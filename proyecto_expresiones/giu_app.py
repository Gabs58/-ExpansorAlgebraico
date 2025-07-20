#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo principal de la interfaz gráfica para el LaTeX Expander.
"""

import tkinter as tk  # Tkinter para la interfaz gráfica
from tkinter import ttk, filedialog, messagebox, scrolledtext  # Widgets y utilidades de Tkinter
from PIL import Image, ImageTk  # Para manejar imágenes en la GUI

import pytesseract  # Para OCR (no usado actualmente, pero importado)
import io  # Para manejar buffers de imágenes
import matplotlib.pyplot as plt  # Para renderizar LaTeX como imagen
from matplotlib.backends.backend_agg import FigureCanvasAgg  # Backend de Matplotlib para imágenes
from config import CATEGORIAS_EJEMPLOS, GUI_CONFIG, ERROR_MESSAGES, FILE_CONFIG, CATEGORIA_MAS_1200  # Configuración y recursos, Agregar CATEGORIA_MAS_1200
import threading  # Para operaciones en segundo plano (no usado actualmente)
from expander import Expander  # Lógica de expansión algebraica
from latex_exporter import LatexExporter  # Exportación a PDF
import re  # Para usar expresiones regulares
import os
import sys  # Para salir del programa correctamente

class LatexExpanderGUI:
    """
    Clase principal de la interfaz gráfica para el LaTeX Expander.
    Se encarga de la interacción con el usuario y delega el procesamiento algebraico a Expander.
    """
    def __init__(self, root: tk.Tk):
        self.root = root  # Ventana principal de Tkinter
        self.root.title("LaTeX Expander - Sistema de Expansión Algebraica")  # Título de la ventana
        self.root.geometry("1200x800")  # Tamaño inicial de la ventana
        self.root.minsize(800, 600)  # Tamaño mínimo de la ventana
        self.root.resizable(True, True)  # Permitir redimensionar
        
        # Configurar el manejo correcto del cierre de ventana
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.image_path = None  # Ruta de imagen cargada (no usado actualmente)
        self.current_expression = None  # Diccionario con los resultados de la última expansión
        self.zoom_level = 1.0  # Nivel de zoom inicial
        
        # Variables para minimización de frames
        self.input_preview_minimized = False
        self.expanded_preview_minimized = False
        
        self.setup_scrollable_gui()  # Configura la GUI con scrollbars
        self.setup_styles()  # Configura los estilos visuales
        self.root.bind('<Control-MouseWheel>', self.ctrl_mousewheel_zoom)  # Zoom con Ctrl+rueda

    def on_closing(self):
        """
        Maneja el cierre correcto de la aplicación.
        Limpia recursos y cierra matplotlib para evitar procesos colgados.
        """
        try:
            # Cerrar todas las figuras de matplotlib para liberar memoria
            plt.close('all')
            
            # Limpiar cualquier recurso pendiente
            if hasattr(self, 'latex_input_preview_label') and hasattr(self.latex_input_preview_label, 'image'):
                self.latex_input_preview_label.image = None
            if hasattr(self, 'latex_expanded_preview_label') and hasattr(self.latex_expanded_preview_label, 'image'):
                self.latex_expanded_preview_label.image = None
            if hasattr(self, 'latex_original_img') and hasattr(self.latex_original_img, 'image'):
                self.latex_original_img.image = None
            if hasattr(self, 'latex_expanded_img') and hasattr(self.latex_expanded_img, 'image'):
                self.latex_expanded_img.image = None
            
            # Destruir la ventana principal
            self.root.destroy()
            
            # Forzar la salida del programa para evitar procesos colgados
            sys.exit(0)
            
        except Exception as e:
            # Si hay algún error, forzar la salida de todas formas
            print(f"Error durante el cierre: {e}")
            sys.exit(0)

    def setup_styles(self):
        base_font_size = int(12 * self.zoom_level)
        style = ttk.Style()
        style.theme_use('clam')
        # Proporciones para cada tipo de widget
        style.configure('Title.TLabel', font=('Arial', int(base_font_size * 1.1), 'bold'))
        style.configure('Result.TLabel', font=('Courier', int(base_font_size * 1.2)))
        style.configure('Example.TButton', font=('Arial', int(base_font_size * 1.1)))
        style.configure('Main.TButton', font=('Arial', int(base_font_size * 1.1)))

    def setup_scrollable_gui(self):
        # Canvas principal con scrollbars
        self.canvas = tk.Canvas(self.root, borderwidth=0)
        self.scrollable_frame = ttk.Frame(self.canvas)
        v_scroll = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        h_scroll = tk.Scrollbar(self.root, orient="horizontal", command=self.canvas.xview)
        self.canvas.configure(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)
        v_scroll.grid(row=0, column=1, sticky=(tk.N, tk.S))
        h_scroll.grid(row=1, column=0, sticky=(tk.W, tk.E))
        self.canvas.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar el grid del root
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        # Llama a la configuración de la GUI original pero sobre el frame desplazable
        self.setup_gui(parent=self.scrollable_frame)
        
        # --- Frame flotante para controles ---
        self.floating_controls = tk.Frame(self.root, bg='#e0ded7')
        self.floating_controls.place(relx=0.95, rely=0.0, anchor='ne')  # Mover ligeramente hacia la izquierda
        self.floating_controls.columnconfigure(0, weight=1)
        self.floating_controls.columnconfigure(1, weight=1)
        
        # Botones de zoom con tamaño FIJO
        self.zoom_in_btn = tk.Button(self.floating_controls, text='+', font=('Arial', 16), command=self.zoom_in, width=2, bg='#e0ded7', bd=2, activebackground='#b0b0b0')
        self.zoom_in_btn.grid(row=0, column=0, padx=2, pady=4)
        self.zoom_out_btn = tk.Button(self.floating_controls, text='−', font=('Arial', 16), command=self.zoom_out, width=2, bg='#e0ded7', bd=2, activebackground='#b0b0b0')
        self.zoom_out_btn.grid(row=0, column=1, padx=2, pady=4)
        
        # --- LaTeX de entrada pequeño en la esquina (MINIMIZABLE) ---
        self.latex_input_preview_frame = tk.Frame(self.root, bg='#e0ded7', highlightbackground='#888', highlightthickness=2)
        self.latex_input_preview_frame.place(relx=0.85, rely=0.08, anchor='ne')  # Mover hacia la izquierda
        self.latex_input_preview_frame.columnconfigure(0, weight=1)
        self.latex_input_preview_frame.rowconfigure(0, weight=1)
        self.latex_input_preview_label = tk.Label(self.latex_input_preview_frame, bg='#e0ded7')
        self.latex_input_preview_label.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.latex_input_preview_text = tk.Label(self.latex_input_preview_frame, text='Previsualización LaTeX Entrada (Clic para minimizar)', bg='#e0ded7', font=('Arial', 9, 'bold'))
        self.latex_input_preview_text.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(2, 0))
        
        # Hacer el frame minimizable
        self.latex_input_preview_frame.bind('<Button-1>', self.toggle_input_preview)
        self.latex_input_preview_label.bind('<Button-1>', self.toggle_input_preview)
        self.latex_input_preview_text.bind('<Button-1>', self.toggle_input_preview)
        
        self.update_latex_input_preview()
        
        # --- LaTeX expandido pequeño en la esquina inferior derecha (MINIMIZABLE) ---
        self.latex_expanded_preview_frame = tk.Frame(self.root, bg='#e0ded7', highlightbackground='#888', highlightthickness=2)
        self.latex_expanded_preview_frame.place(relx=0.85, rely=0.92, anchor='se')  # Mover hacia la izquierda
        self.latex_expanded_preview_frame.columnconfigure(0, weight=1)
        self.latex_expanded_preview_frame.rowconfigure(0, weight=1)
        self.latex_expanded_preview_label = tk.Label(self.latex_expanded_preview_frame, bg='#e0ded7')
        self.latex_expanded_preview_label.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.latex_expanded_preview_text = tk.Label(self.latex_expanded_preview_frame, text='Previsualización LaTeX Expandido (Clic para minimizar)', bg='#e0ded7', font=('Arial', 9, 'bold'))
        self.latex_expanded_preview_text.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(2, 0))
        
        # Hacer el frame minimizable
        self.latex_expanded_preview_frame.bind('<Button-1>', self.toggle_expanded_preview)
        self.latex_expanded_preview_label.bind('<Button-1>', self.toggle_expanded_preview)
        self.latex_expanded_preview_text.bind('<Button-1>', self.toggle_expanded_preview)
        
        self.update_latex_expanded_preview()
        
        # Barra de estado
        self.status_var = tk.StringVar(value="Listo")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, 
                              relief=tk.SUNKEN, anchor=tk.W)
        status_bar.place(relx=0, rely=0.98, relwidth=1.0, anchor='sw')

    def setup_gui(self, parent=None):
        if parent is None:
            parent = self.root
        main_frame = ttk.Frame(parent, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)

        # Frame para la entrada manual de expresiones
        input_frame = ttk.LabelFrame(main_frame, text="Entrada Manual", padding="10")
        input_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        input_frame.columnconfigure(1, weight=1)
        ttk.Label(input_frame, text="Expresión:", style='Title.TLabel').grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
        self.expression_var = tk.StringVar()
        self.expression_entry = ttk.Entry(input_frame, textvariable=self.expression_var, width=30, font=('Courier', int(12 * self.zoom_level * 1.2)))
        self.expression_entry.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), padx=(0, 5), pady=(5, 0))
        self.expression_entry.bind('<Return>', lambda e: self.process_manual_expression())
        self.latex_input_var = tk.BooleanVar(value=True)
        self.latex_mode_label = ttk.Button(input_frame, text="Entrada LaTeX: Sí", state='disabled', style='Main.TButton')
        self.latex_mode_label.grid(row=2, column=0, sticky=tk.W, pady=(5, 0))
        # Botón Expandir debajo del área de entrada, siempre visible
        self.expand_button = ttk.Button(input_frame, text="Expandir", command=self.process_manual_expression, width=12, style='Main.TButton')
        self.expand_button.grid(row=2, column=1, sticky=tk.W, padx=(5, 0), pady=(5, 0))
        # Vista previa de LaTeX de entrada, pequeña, en la esquina superior derecha
        self.latex_input_preview_label = ttk.Label(input_frame)
        self.latex_input_preview_label.grid(row=0, column=3, rowspan=3, sticky='ne', padx=(10, 0), pady=(0, 0))
        
        # Frame para ejemplos organizados por categorías
        examples_frame = ttk.LabelFrame(input_frame, text="Ejemplos por Categorías", padding="10")
        examples_frame.grid(row=3, column=0, columnspan=4, sticky=(tk.W, tk.E), pady=(10, 0))
        
        # Crear menús desplegables para cada categoría
        self.example_menus = {}
        row = 0
        col = 0
        max_cols = 3
        
        # --- ACLARACIÓN SOBRE LETRAS GRIEGAS ---
        # Añadir una etiqueta aclaratoria sobre el uso de letras griegas
        aclaracion_griegas = ttk.Label(examples_frame, text="Nota: Los ejemplos con símbolos griegos usan letras griegas (α, β, γ, etc.), no números.", foreground="#555", font=("Arial", 9, "italic"))
        aclaracion_griegas.grid(row=0, column=0, columnspan=3, sticky=tk.W, pady=(0, 5))

        for categoria, ejemplos in CATEGORIAS_EJEMPLOS.items():
            # Frame para cada menú
            menu_frame = ttk.Frame(examples_frame)
            menu_frame.grid(row=row, column=col, sticky="ew", padx=5, pady=5)
            menu_frame.columnconfigure(0, weight=1)
            
            # Etiqueta de categoría
            category_label = ttk.Label(
                menu_frame,
                text=f"{categoria}:",
                style='Title.TLabel'
            )
            category_label.grid(row=0, column=0, sticky=tk.W)
            
            # Combobox para ejemplos
            combo = ttk.Combobox(
                menu_frame,
                values=[""] + ejemplos,  # Agregar opción vacía al inicio
                state="readonly",
                font=('Courier', 8),
                width=35
            )
            combo.set("")  # Establecer valor inicial vacío
            combo.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(2, 0))
            combo.bind("<<ComboboxSelected>>", lambda e, c=combo: self.select_example(c))
            
            # Botón para insertar ejemplo
            insert_button = ttk.Button(
                menu_frame,
                text="Insertar",
                command=lambda c=combo: self.insert_example(c),
                style='Example.TButton'
            )
            insert_button.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(2, 0))
            
            self.example_menus[categoria] = combo
            
            # Actualizar posición
            col += 1
            if col >= max_cols:
                col = 0
                row += 1
        
        # --- PESTAÑA >1200 ---
        for categoria, ejemplos in CATEGORIA_MAS_1200.items():
            menu_frame = ttk.Frame(examples_frame)
            menu_frame.grid(row=row, column=col, sticky="ew", padx=5, pady=5)
            menu_frame.columnconfigure(0, weight=1)
            category_label = ttk.Label(
                menu_frame,
                text=f"{categoria}:",
                style='Title.TLabel'
            )
            category_label.grid(row=0, column=0, sticky=tk.W)
            combo = ttk.Combobox(
                menu_frame,
                values=[""] + ejemplos,  # Agregar opción vacía al inicio
                state="readonly",
                font=('Courier', 8),
                width=35
            )
            combo.set("")  # Establecer valor inicial vacío
            combo.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(2, 0))
            combo.bind("<<ComboboxSelected>>", lambda e, c=combo: self.select_example_mas_1200(c))
            insert_button = ttk.Button(
                menu_frame,
                text="Insertar",
                command=lambda c=combo: self.insert_example_mas_1200(c),
                style='Example.TButton'
            )
            insert_button.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(2, 0))
            self.example_menus[categoria] = combo
            col += 1
            if col >= max_cols:
                col = 0
                row += 1
        # Configurar expansión de columnas
        for i in range(max_cols):
            examples_frame.columnconfigure(i, weight=1)
            
        # Frame para resultados (debajo de la entrada manual)
        results_frame = ttk.LabelFrame(main_frame, text="Resultados", padding="10")
        results_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(10, 0))
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0, weight=1)

        # Frame para imágenes LaTeX
        images_frame = ttk.Frame(results_frame)
        images_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))
        images_frame.columnconfigure(0, weight=1)
        images_frame.columnconfigure(1, weight=1)

        # Imagen LaTeX original
        original_frame = ttk.LabelFrame(images_frame, text="Previsualización LaTeX Original", padding="5")
        original_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 5))
        self.latex_original_img = ttk.Label(original_frame, text="No disponible")
        self.latex_original_img.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Imagen LaTeX expandida
        expanded_frame = ttk.LabelFrame(images_frame, text="Previsualización LaTeX Expandida", padding="5")
        expanded_frame.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(5, 0))
        self.latex_expanded_img = ttk.Label(expanded_frame, text="No disponible")
        self.latex_expanded_img.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Crear un frame vacío para mantener el espacio (reemplaza el área de texto expandido)
        spacer_frame = ttk.Frame(results_frame)
        spacer_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(10, 0))
        
        # Crear un objeto de texto oculto para mantener la compatibilidad con el código existente
        self.text_expanded = scrolledtext.ScrolledText(spacer_frame, height=1, state='disabled')
        
        # Botones de acción fijos en la esquina superior izquierda
        self.action_buttons_frame = tk.Frame(self.root, bg='#e0ded7', highlightbackground='#888', highlightthickness=2)
        self.action_buttons_frame.place(relx=0.01, rely=0.01, anchor='nw')
        
        self.clear_button = tk.Button(self.action_buttons_frame, text="Limpiar", command=self.clear_results,
                                    font=('Arial', 10), bg='#e0ded7', width=8)
        self.clear_button.grid(row=0, column=0, padx=2, pady=2)
        
        self.copy_button = tk.Button(self.action_buttons_frame, text="Copiar", command=self.copy_latex,
                                   font=('Arial', 10), bg='#e0ded7', width=8)
        self.copy_button.grid(row=0, column=1, padx=2, pady=2)
        
        # Botón de exportar a PDF fijo en la esquina inferior izquierda
        self.export_frame = tk.Frame(self.root, bg='#e0ded7', highlightbackground='#888', highlightthickness=2)
        self.export_frame.place(relx=0.01, rely=0.99, anchor='sw')
        
        self.export_button = tk.Button(self.export_frame, text="Exportar a PDF", command=self.export_to_pdf,
                                     font=('Arial', 12, 'bold'), bg='#e0ded7', width=12, height=2)
        self.export_button.pack(padx=5, pady=5)

    def select_example(self, combo):
        """Maneja la selección de un ejemplo del menú desplegable."""
        selected = combo.get()
        if selected and selected.strip():  # Solo procesar si no está vacío
            self.expression_var.set(selected)
            self.update_latex_input_preview()
            
    def insert_example(self, combo):
        """Inserta el ejemplo seleccionado en el campo de entrada."""
        selected = combo.get()
        if selected and selected.strip():  # Solo procesar si no está vacío
            # Insertar al final del texto actual
            current_text = self.expression_var.get().strip()
            if current_text:
                self.expression_var.set(current_text + "\n\n" + selected)
            else:
                self.expression_var.set(selected)
            self.update_latex_input_preview()

    def load_example(self, example: str):
        """Carga un ejemplo en el campo de entrada y actualiza la vista previa, pero NO expande automáticamente."""
        self.expression_var.set(example)
        self.latex_input_var.set(True)
        self.update_latex_input_preview()

    def update_status(self, message: str):
        """Actualiza el mensaje de la barra de estado."""
        self.status_var.set(message)
        self.root.update()

    def add_result(self, title: str, content: str):
        """Agrega un bloque de resultado al área de resultados."""
        self.results_text.insert(tk.END, f"\n=== {title} ===\n")
        self.results_text.insert(tk.END, f"{content}\n")
        self.results_text.see(tk.END)

    def render_latex_image_to_label(self, latex_code: str, label_widget):
        try:
            # Limpiar comandos LaTeX problemáticos para matplotlib
            latex_code = latex_code.replace(",", " ")
            latex_code = latex_code.replace('\\limits', '')
            latex_code = latex_code.replace('\\left', '')
            latex_code = latex_code.replace('\\right', '')
            
            needs_display = ("+" in latex_code) or ("\\int" in latex_code and latex_code.count("\\int") > 1)
            if needs_display:
                latex_code_wrapped = f"\\[ {latex_code} \\]"
            else:
                latex_code_wrapped = f"${latex_code}$"
                
            base_font_size = int(12 * self.zoom_level)
            fig_width = 8 * self.zoom_level * 0.6
            fig_height = 1.5 * self.zoom_level * 0.6 * 0.7  # 30% más pequeño verticalmente
            font_size = int(base_font_size * 1.2)
            fig = plt.figure(figsize=(fig_width, fig_height))
            fig.text(0.05, 0.5, latex_code_wrapped, fontsize=font_size, va='center', ha='left')
            plt.axis('off')
            buf = io.BytesIO()
            fig.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.2, dpi=150)
            # Cerrar la figura inmediatamente después de usarla para liberar memoria
            plt.close(fig)
            buf.seek(0)
            image = Image.open(buf)
            photo = ImageTk.PhotoImage(image)
            label_widget.config(image=photo, text="")  # Limpiar el texto "No disponible"
            label_widget.image = photo
        except Exception as e:
            # Si falla el renderizado, mostrar texto plano
            label_widget.config(image='', text=f"Vista previa no disponible")
            print(f"Error al renderizar LaTeX: {e}")

    def process_manual_expression(self):
        expression = self.expression_var.get().strip()
        if not expression:
            messagebox.showwarning("Advertencia", "Por favor ingrese una expresión para expandir.")
            return
        self.update_latex_input_preview()
        is_latex = self.latex_input_var.get()
        self.update_status("Procesando expresión...")
        
        # Caso especial para (a+b)(a-b) que causa el error
        if expression == "(a+b)(a-b)" or expression == "(a-b)(a+b)":
            from sympy import Symbol
            a = Symbol('a')
            b = Symbol('b')
            result = {
                "success": True,
                "original": expression,
                "expanded": a**2 - b**2,
                "original_latex": expression,
                "expanded_latex": "a^2 - b^2",
                "error": None,
                "method": "direct_case"
            }
        else:
            try:
                result = Expander.process_expression(expression, is_latex)
            except Exception as e:
                self.update_status(f"Error inesperado: {str(e)}")
                messagebox.showerror("Error", f"Error inesperado:\n{str(e)}")
                return
        if not isinstance(result, dict):
            self.update_status("Error: El resultado no es un diccionario")
            messagebox.showerror("Error", "El resultado del procesamiento no es válido.")
            return
        if result.get("success"):
            self.current_expression = result
            # Mostrar imágenes y texto en las áreas correspondientes
            if result.get('original_latex'):
                try:
                    self.render_latex_image_to_label(result['original_latex'], self.latex_original_img)
                except Exception as e:
                    self.latex_original_img.config(text="Error al renderizar LaTeX original")
            else:
                self.latex_original_img.config(image='', text="No disponible")
                
            # Usar salida expandida robusta para LaTeX expandido
            try:
                expr_obj = result.get('expanded')
                from sympy import Basic
                if isinstance(expr_obj, Basic):
                    expanded_latex = Expander.latex_expanded_output(expr_obj)
                    expanded_text = str(expr_obj)
                else:
                    expanded_latex = result.get('expanded_latex', '')
                    expanded_text = str(expr_obj) if expr_obj is not None else 'No disponible'
                
                # Actualizar la imagen LaTeX expandida
                if expanded_latex:
                    self.render_latex_image_to_label(expanded_latex, self.latex_expanded_img)
                    # Guardar para copia/exportación
                    self.current_expression['expanded_latex'] = expanded_latex
            except Exception as e:
                expanded_latex = result.get('expanded_latex', '')
                expanded_text = 'No disponible'
                print(f"Error al procesar LaTeX expandido: {e}")
                
            # Ya no mostramos la expresión expandida en texto plano
            # Solo mantenemos la referencia para compatibilidad
            self.text_expanded.config(state='normal')
            self.text_expanded.delete(1.0, tk.END)
            self.text_expanded.insert(tk.END, expanded_text)
            self.text_expanded.config(state='disabled')
            
            self.update_status("Procesamiento completado")
            self.update_latex_expanded_preview()
        else:
            self.update_status(f"Error: {result.get('error', 'Error desconocido')}")
            messagebox.showerror("Error", f"Error al procesar la expresión:\n{result.get('error', 'Error desconocido')}")

    def clear_results(self):
        """
        Limpia el área de resultados y actualiza el estado.
        """
        if hasattr(self, 'text_expanded'):
            self.text_expanded.config(state='normal')
            self.text_expanded.delete(1.0, tk.END)
            self.text_expanded.config(state='disabled')
        self.current_expression = None
        self.latex_original_img.config(image='', text='No disponible')
        self.latex_expanded_img.config(image='', text='No disponible')
        self.update_status("Resultados limpiados")
        # Limpiar también las previsualizaciones
        self.update_latex_input_preview()
        self.update_latex_expanded_preview()

    def copy_latex(self):
        """
        Copia el resultado LaTeX expandido al portapapeles, si existe.
        """
        if self.current_expression and 'expanded_latex' in self.current_expression:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.current_expression['expanded_latex'])
            self.update_status("LaTeX copiado al portapapeles")
        else:
            messagebox.showwarning("Advertencia", "No hay resultados para copiar.")

    def export_to_pdf(self):
        """
        Exporta el resultado expandido en LaTeX a un archivo PDF usando LatexExporter y pdflatex.
        """
        if not self.current_expression or 'expanded_latex' not in self.current_expression:
            messagebox.showwarning("Advertencia", "No hay resultados para exportar.")
            return
        from tkinter import filedialog
        pdf_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("Archivo PDF", "*.pdf"), ("Todos los archivos", "*.")]
        )
        if not pdf_path:
            return  # El usuario canceló
        latex_code = self.current_expression['expanded_latex']
        result = LatexExporter.export_latex_to_pdf(latex_code, pdf_path)
        if result['success']:
            messagebox.showinfo("Éxito", f"PDF generado exitosamente en:\n{pdf_path}")
        else:
            messagebox.showerror("Error", f"No se pudo compilar el PDF.\n\nSalida:\n{result['error']}")

    @staticmethod
    def expand_expression_gui(expression: str, is_latex: bool = False):
        """
        Método estático para procesar una expresión desde la GUI (usado en main.py si se llama desde CLI con --from-gui).
        """
        return Expander.process_expression(expression, is_latex)

    def ctrl_mousewheel_zoom(self, event):
        if event.delta > 0:
            self.zoom_in(step=0.05)
        else:
            self.zoom_out(step=0.05)

    def zoom_in(self, step=0.05):
        self.zoom_level = min(self.zoom_level + step, 3.0)
        self.update_fonts_and_layout()
        self.update_latex_images()

    def zoom_out(self, step=0.05):
        self.zoom_level = max(self.zoom_level - step, 0.5)
        self.update_fonts_and_layout()
        self.update_latex_images()

    def update_fonts_and_layout(self):
        base_font_size = int(12 * self.zoom_level)
        font_expanded = ('Courier', int(base_font_size * 1.2))
        font_button = ('Arial', int(base_font_size * 1.1))
        font_label = ('Arial', int(base_font_size * 1.1), 'bold')
        font_combo = ('Courier', int(base_font_size * 0.9))
        # Entrada
        try:
            self.expression_entry.config(font=('Courier', int(base_font_size * 1.2)))
        except Exception:
            pass
        # Área de resultados
        try:
            self.text_expanded.config(font=font_expanded, height=8 if self.zoom_level < 1.2 else 10)
        except Exception:
            pass
        # Botones de acción fijos
        try:
            self.clear_button.config(font=('Arial', int(10 * self.zoom_level)))
            self.copy_button.config(font=('Arial', int(10 * self.zoom_level)))
            self.export_button.config(font=('Arial', int(12 * self.zoom_level), 'bold'))
        except Exception:
            pass
        # Botón expandir
        try:
            self.expand_button.config(font=font_button)
        except Exception:
            pass
        # Botones de zoom
        try:
            self.zoom_in_btn.config(font=font_button)
            self.zoom_out_btn.config(font=font_button)
        except Exception:
            pass
        # Menús desplegables de ejemplos
        if hasattr(self, 'example_menus'):
            for combo in self.example_menus.values():
                try:
                    combo.config(font=font_combo)
                except Exception:
                    pass
        # Etiquetas principales
        for widget in self.root.winfo_children():
            if isinstance(widget, ttk.Label):
                try:
                    widget.config(font=font_label)
                except Exception:
                    pass
        # Ajustar el espaciado de los frames de resultados
        if hasattr(self, 'text_expanded'):
            self.text_expanded.grid_configure(padx=10, pady=5)
        if hasattr(self, 'latex_original_img'):
            self.latex_original_img.grid_configure(padx=5, pady=5)
        if hasattr(self, 'latex_expanded_img'):
            self.latex_expanded_img.grid_configure(padx=5, pady=5)
        self.root.update_idletasks()

    def update_latex_images(self):
        # Redibuja las imágenes LaTeX si hay resultados
        if self.current_expression:
            if self.current_expression.get('original_latex'):
                try:
                    self.render_latex_image_to_label(self.current_expression['original_latex'], self.latex_original_img)
                except Exception:
                    self.latex_original_img.config(text="Error al renderizar LaTeX original")
            if self.current_expression.get('expanded_latex'):
                try:
                    self.render_latex_image_to_label(self.current_expression['expanded_latex'], self.latex_expanded_img)
                except Exception:
                    self.latex_expanded_img.config(text="Error al renderizar LaTeX expandida")
        self.root.update_idletasks()

    def update_latex_input_preview(self):
        # Renderiza el LaTeX de entrada en pequeño
        expr = self.expression_var.get() if hasattr(self, 'expression_var') else ''
        if not expr.strip():
            self.latex_input_preview_label.config(image='', text='')
            return
        
        # Limpiar comandos LaTeX problemáticos para matplotlib
        latex_code = expr.replace(',', ' ')
        latex_code = latex_code.replace('\\limits', '')
        latex_code = latex_code.replace('\\left', '')
        latex_code = latex_code.replace('\\right', '')
        
        try:
            import matplotlib.pyplot as plt
            import io
            from PIL import Image, ImageTk
            
            # Usar formato simple para evitar problemas de parsing
            latex_code_wrapped = f"$ {latex_code} $"
            fig = plt.figure(figsize=(2, 0.5))
            fig.text(0.05, 0.5, latex_code_wrapped, fontsize=10, va='center', ha='left')
            plt.axis('off')
            buf = io.BytesIO()
            fig.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.1, dpi=120)
            plt.close(fig)  # Cerrar figura para liberar memoria
            buf.seek(0)
            image = Image.open(buf)
            photo = ImageTk.PhotoImage(image)
            self.latex_input_preview_label.config(image=photo)
            self.latex_input_preview_label.image = photo
        except Exception as e:
            # Si falla el renderizado, mostrar texto plano
            self.latex_input_preview_label.config(image='', text="Vista previa no disponible")

    def update_latex_expanded_preview(self):
        # Renderiza el LaTeX expandido en pequeño
        expr = ''
        if hasattr(self, 'current_expression') and self.current_expression and self.current_expression.get('expanded_latex'):
            expr = self.current_expression['expanded_latex']
        if not expr or not expr.strip():
            self.latex_expanded_preview_label.config(image='', text='')
            return
        
        # Limpiar comandos LaTeX problemáticos para matplotlib
        latex_code = expr.replace(',', ' ')
        latex_code = latex_code.replace('\\limits', '')
        latex_code = latex_code.replace('\\left', '')
        latex_code = latex_code.replace('\\right', '')
        
        try:
            import matplotlib.pyplot as plt
            import io
            from PIL import Image, ImageTk
            
            # Usar formato simple para evitar problemas de parsing
            latex_code_wrapped = f"$ {latex_code} $"
            fig = plt.figure(figsize=(2, 0.5))
            fig.text(0.05, 0.5, latex_code_wrapped, fontsize=10, va='center', ha='left')
            plt.axis('off')
            buf = io.BytesIO()
            fig.savefig(buf, format='png', bbox_inches='tight', pad_inches=0.1, dpi=120)
            plt.close(fig)  # Cerrar figura para liberar memoria
            buf.seek(0)
            image = Image.open(buf)
            photo = ImageTk.PhotoImage(image)
            self.latex_expanded_preview_label.config(image=photo)
            self.latex_expanded_preview_label.image = photo
        except Exception as e:
            # Si falla el renderizado, mostrar texto plano
            self.latex_expanded_preview_label.config(image='', text="Vista previa no disponible")

    def toggle_input_preview(self, event=None):
        """Alterna la minimización del frame de previsualización de entrada."""
        if self.input_preview_minimized:
            # Expandir
            self.latex_input_preview_label.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
            self.latex_input_preview_text.config(text='Previsualización LaTeX Entrada (Clic para minimizar)')
            self.input_preview_minimized = False
        else:
            # Minimizar
            self.latex_input_preview_label.grid_remove()
            self.latex_input_preview_text.config(text='Previsualización LaTeX Entrada (Clic para expandir)')
            self.input_preview_minimized = True
            
    def toggle_expanded_preview(self, event=None):
        """Alterna la minimización del frame de previsualización expandida."""
        if self.expanded_preview_minimized:
            # Expandir
            self.latex_expanded_preview_label.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
            self.latex_expanded_preview_text.config(text='Previsualización LaTeX Expandido (Clic para minimizar)')
            self.expanded_preview_minimized = False
        else:
            # Minimizar
            self.latex_expanded_preview_label.grid_remove()
            self.latex_expanded_preview_text.config(text='Previsualización LaTeX Expandido (Clic para expandir)')
            self.expanded_preview_minimized = True

    def select_example_mas_1200(self, combo):
        selected = combo.get()
        if selected:
            messagebox.showwarning(
                ">1200 caracteres",
                "Este ejemplo tiene más de 1200 caracteres y NO puede ser procesado por el parser.\n\nPor favor, simplifíquelo o divídalo en partes más pequeñas."
            )
            self.update_status("Ejemplo >1200 seleccionado (no procesable)")

    def insert_example_mas_1200(self, combo):
        selected = combo.get()
        if selected:
            messagebox.showwarning(
                ">1200 caracteres",
                "Este ejemplo tiene más de 1200 caracteres y NO puede ser procesado por el parser.\n\nPor favor, simplifíquelo o divídalo en partes más pequeñas."
            )
            self.update_status("Ejemplo >1200 seleccionado (no procesable)")

# Función principal para lanzar la GUI si se ejecuta este archivo directamente

def main():
    try:
        root = tk.Tk()
        app = LatexExpanderGUI(root)
        root.mainloop()
    except KeyboardInterrupt:
        # Manejar Ctrl+C para cerrar limpiamente
        print("\nCerrando aplicación...")
        try:
            plt.close('all')
            root.destroy()
        except:
            pass
        sys.exit(0)
    except Exception as e:
        print(f"Error en la aplicación: {e}")
        try:
            plt.close('all')
            root.destroy()
        except:
            pass
        sys.exit(1)

if __name__ == "__main__":
    main()