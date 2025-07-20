# ExpaAlgebraico - Documentación Técnica

## Información del Proyecto
- **Nombre:** ExpaAlgebraico
- **Versión:** 1.0.0
- **Autor:** Gabriel Bustos
- **Fecha:** 2025
- **Licencia:** Educativa.

## Descripción Técnica

ExpaAlgebraico es un sistema de procesamiento algebraico especializado en la expansión de expresiones matemáticas escritas en notación LaTeX. El sistema convierte productos de factores polinómicos en sumas o diferencias de términos, manteniendo la sintaxis LaTeX tanto en entrada como en salida.

### Premisa Fundamental
El sistema está diseñado para expandir expresiones que cumplen la siguiente premisa:
> **Expandir una expresión escrita como producto de factores (cada factor es a lo más un polinomio) a una expresión escrita como suma o diferencia de términos (un polinomio).**

## Arquitectura del Sistema

### Componentes Principales

#### 1. **InputParser** (`input_parser.py`)
- **Responsabilidad:** Conversión de expresiones LaTeX a objetos SymPy, identificando el tipo de expresión y aplicando reglas de reescritura y estrategias de parsing específicas.
- **Funciones principales:**
  - `parse_latex(expression)`: Identifica el tipo de expresión (sumatoria, integral, derivada, trigonométrica, binomio, etc.) y aplica la estrategia óptima.
  - `_rewrite_*_robust()`: Reescritura robusta para cada tipo de expresión.
  - `_clean_expression_body_robust()`: Limpieza avanzada de subíndices, griegas, multiplicación implícita y comandos LaTeX.
  - Fallbacks específicos para cada tipo, garantizando siempre una salida válida.


**Robustez:**
- El parser nunca muestra errores técnicos al usuario y siempre entrega un resultado válido o una sugerencia clara.
- Modularidad total para mejora gradual y trazabilidad por tipo de expresión.

#### 2. **Expander** (`expander.py`)
- **Responsabilidad:** Lógica de expansión algebraica
- **Funciones principales:**
  - `process_expression(expression, is_latex)`: Procesamiento principal
  - `expand_expression(expr)`: Expansión usando SymPy
  - `expand_and_simplify(expr)`: Expansión con simplificación

#### 3. **LatexExporter** (`latex_exporter.py`)
- **Responsabilidad:** Conversión de SymPy a LaTeX y exportación
- **Funciones principales:**
  - `to_latex(expr)`: Conversión a LaTeX compatible con matplotlib
  - `export_latex_to_pdf(latex_code, output_path)`: Exportación a PDF

#### 4. **GUI** (`giu app.py`)
- **Responsabilidad:** Interfaz gráfica de usuario
- **Características:**
  - Renderizado de LaTeX con matplotlib
  - Sistema de zoom y navegación
  - Categorización de ejemplos
  - Exportación a PDF

## Especificaciones Técnicas

### Dependencias Principales
```
sympy>=1.12.0          # Álgebra simbólica
latex2sympy2>=1.0.0    # Conversión LaTeX a SymPy
matplotlib>=3.7.0      # Renderizado de LaTeX
tkinter                # Interfaz gráfica (incluido en Python)
PIL>=9.5.0             # Procesamiento de imágenes
```

### Estructura de Datos

#### Resultado de Procesamiento
```python
{
    "success": bool,           # Estado de la operación
    "original": str,           # Expresión original en texto
    "expanded": str,           # Expresión expandida en texto
    "original_latex": str,     # LaTeX de la expresión original
    "expanded_latex": str,     # LaTeX de la expresión expandida
    "error": str               # Mensaje de error (si aplica)
}
```

### Algoritmos Implementados

#### 1. Preprocesamiento de LaTeX
- Eliminación de delimitadores `\left`, `\right`
- Normalización de subíndices (`x_1` → `x1`)
- Conversión de letras griegas
- Inserción de multiplicación explícita
- Eliminación de comandos problemáticos (`\limits`, `\mathrm`)

#### 2. Postprocesamiento para Visualización
- Limpieza de comandos incompatibles con matplotlib
- Normalización de integrales
- Simplificación de fracciones complejas

#### 3. Expansión Algebraica
- Uso de `sympy.expand()` para expansión
- Manejo de errores robusto
- Validación de resultados

## Configuración del Sistema

### Archivo de Configuración (`config.py`)
- **CATEGORIAS_EJEMPLOS:** Organización de ejemplos por categorías
- **EJEMPLOS_CHEAT_SHEET:** Ejemplos avanzados con notación `\left( ... \right)`
- **ERROR_MESSAGES:** Mensajes de error estandarizados
- **FILE_CONFIG:** Configuración de archivos

### Variables de Entorno
- **PYTHONPATH:** Configuración de rutas de módulos
- **LATEX_PATH:** Ruta a instalación de LaTeX (para exportación PDF)

## Manejo de Errores

### Tipos de Errores
1. **Errores de Parsing:** Expresiones LaTeX malformadas
2. **Errores de Expansión:** Expresiones que no cumplen la premisa
3. **Errores de Renderizado:** Problemas con matplotlib
4. **Errores de Exportación:** Fallos en compilación LaTeX

### Estrategia de Recuperación
- Preprocesamiento robusto para casos límite
- Postprocesamiento para compatibilidad de visualización
- Manejo de excepciones en cada capa
- Mensajes de error informativos

## Rendimiento y Optimización

### Optimizaciones Implementadas
- Cierre automático de figuras matplotlib para liberar memoria
- Preprocesamiento eficiente con expresiones regulares
- Caché de conversiones LaTeX
- Manejo de recursos en GUI

### Límites del Sistema
- **Complejidad:** Expresiones de hasta grado 8-10
- **Memoria:** Gestión automática de recursos matplotlib
- **Tiempo:** Procesamiento en tiempo real para expresiones típicas


## Mantenimiento

### Logs y Debugging
- Mensajes de estado en GUI
- Manejo de excepciones detallado 
- Validación de resultados
- sitema de debug y login para identificar tipó de error

### Actualizaciones
- Compatibilidad con nuevas versiones de SymPy
- Actualización de dependencias LaTeX
- Mejoras en preprocesamiento

---
