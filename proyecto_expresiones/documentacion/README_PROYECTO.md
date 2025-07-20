# ExpaAlgebraico - Sistema de Expansión Algebraica

## Descripción del Proyecto

ExpaAlgebraico es un sistema especializado en el procesamiento y expansión de expresiones algebraicas escritas en notación LaTeX. El sistema está diseñado para estudiantes, profesores e investigadores que necesitan expandir productos de factores polinómicos de manera eficiente y precisa.

### Objetivo Principal
El sistema cumple una premisa fundamental específica:
> **Expandir una expresión escrita como producto de factores (cada factor es a lo más un polinomio) a una expresión escrita como suma o diferencia de términos (un polinomio).**

## Características Principales

### **Especialización Matemática**
- Procesamiento exclusivo de productos de factores polinómicos
- Expansión algebraica precisa usando SymPy
- Mantenimiento de la notación LaTeX en entrada y salida

### **Interfaz Gráfica Avanzada**
- GUI intuitiva con renderizado de LaTeX en tiempo real
- Sistema de zoom y navegación
- Categorización de ejemplos por dificultad
- Vista previa de entrada y salida

### **Biblioteca de Ejemplos**
- **Básicos:** Expresiones simples para iniciación
- **Intermedios:** Casos con múltiples variables y potencias
- **Avanzados:** Expresiones complejas con funciones trigonométricas
- **Cheat Sheet:** Ejemplos con notación `\left( ... \right)` profesional

### **Herramientas de Exportación**
- Conversión automática a LaTeX compatible con matplotlib
- Exportación directa a PDF
- Copia al portapapeles para uso en documentos

## Casos de Uso

### Para Estudiantes
- **Práctica de álgebra:** Verificar expansiones manuales
- **Aprendizaje:** Ver paso a paso cómo se expanden expresiones
- **Tareas:** Generar resultados precisos para trabajos académicos

### Para Profesores
- **Preparación de material:** Crear ejemplos expandidos rápidamente
- **Verificación:** Comprobar resultados de ejercicios
- **Presentaciones:** Exportar expresiones a PDF para documentos

### Para Investigadores
- **Análisis matemático:** Procesar expresiones complejas
- **Documentación:** Generar LaTeX para papers y artículos
- **Validación:** Verificar cálculos algebraicos

## Ejemplos de Uso

### Expresión Básica
**Entrada:** `(x+1)(x-1)`
**Salida:** `x^2 - 1`

### Expresión con Notación LaTeX
**Entrada:** `\left(x^2 + 2x + 1\right)\left(x^2 - 2x + 1\right)`
**Salida:** `x^4 - 2x^2 + 1`

### Expresión con Funciones
**Entrada:** `\sin(x)(x^2 + 1)`
**Salida:** `\sin(x) \cdot x^2 + \sin(x)`

## Instalación y Configuración

### Requisitos del Sistema
- Python 3.12 
- Dependencias listadas en `requirements.txt`
- Opcional: LaTeX para exportación a PDF

### Instalación Rápida
```bash
# Clonar el repositorio
git clone [URL_DEL_REPOSITORIO]

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la GUI
python "proyecto_expresiones/giu app.py"
```

### Archivos de Ejecución
- `ejecutar_gui.bat` - Ejecuta la interfaz gráfica
- `instalar_dependencias.bat` - Instala dependencias automáticamente

## Estructura del Proyecto

```
ExpaAlgebraico/
├── proyecto_expresiones/
│   ├── giu app.py              # Interfaz gráfica principal
│   ├── input_parser.py         # Parser de entrada LaTeX
│   ├── expander.py             # Lógica de expansión
│   ├── latex_exporter.py       # Exportación a LaTeX/PDF
│   ├── config.py               # Configuración y ejemplos
│   ├── utils.py                # Utilidades auxiliares
│   └── main.py                 # Punto de entrada CLI
├── README_TECNICO.md           # Documentación técnica
├── README_PROYECTO.md          # Esta documentación
├── README_USUARIO.md           # Guía de usuario
├── README_desarrolador.md      # Dependencias
└── venv312/                    # Entorno virtual
```

## Limitaciones y Consideraciones

### Alcance del Sistema
- **Solo productos de factores:** No procesa sumas o diferencias directamente
- **Factores polinómicos:** Cada factor debe ser a lo más un polinomio
- **Notación LaTeX:** Entrada y salida en formato LaTeX

### Casos No Soportados
- Expresiones que no son productos de factores
- Factores que no son polinomios (funciones trascendentes complejas)
- Expresiones con límites infinitos o series
- Derivadas de orden superior a 2

### Rendimiento
- **Expresiones simples:** Procesamiento instantáneo
- **Expresiones complejas:** Hasta grado 8-10 eficientemente
- **Memoria:** Gestión automática de recursos

## Contribuciones y Desarrollo

### Estándares de Código
- Documentación completa en español
- Manejo robusto de errores
- Compatibilidad con matplotlib
- Código comentado y estructurado

### Mejoras Futuras
- Soporte para más tipos de funciones
- Integración con sistemas de álgebra computacional
- API para integración con otros sistemas
- Soporte para expresiones vectoriales

## Soporte y Contacto

### Información del Autor
- **Desarrollador:** Gabriel Bustos
- **Institución:** Universidad Nacional de Colombia
- **Año:** 2025

### Reporte de Problemas
Para reportar errores o solicitar mejoras:
1. Verificar que el problema cumple la premisa del sistema
2. Incluir la expresión de entrada exacta
3. Describir el comportamiento esperado vs. actual

## Licencia

Este proyecto es propiedad intelectual de Gabriel Bustos. uso educativo.

---

*ExpaAlgebraico v1.0.0 - Sistema de Expansión Algebraica Profesional* 
