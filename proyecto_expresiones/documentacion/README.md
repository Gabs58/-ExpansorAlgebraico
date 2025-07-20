# ExpaAlgebraico - Sistema de Expansión Algebraica

## Descripción

ExpaAlgebraico es un sistema especializado en la expansión de expresiones algebraicas escritas en notación LaTeX. El sistema convierte productos de factores polinómicos en sumas o diferencias de términos, manteniendo la sintaxis LaTeX tanto en entrada como en salida.

### Premisa Fundamental
> **Expandir una expresión escrita como producto de factores (cada factor es a lo más un polinomio) a una expresión escrita como suma o diferencia de términos (un polinomio).**

## Características Principales

- **Especialización matemática** en productos de factores polinómicos
- **Interfaz gráfica avanzada** con renderizado LaTeX en tiempo real
- **Biblioteca de ejemplos** organizados por categorías
- **Herramientas de exportación** (LaTeX, PDF)
- **Sistema de zoom** y navegación intuitiva

## Instalación Rápida

### Para Python 3.12 (Recomendado)
```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la GUI
python "proyecto_expresiones/giu app.py"
```

### Para Python 3.13 (Solución de compatibilidad)
```bash
# Usar el script específico para Python 3.13
instalar_dependencias_python313.bat

# O ejecutar manualmente:
pip install antlr4-python3-runtime==4.7.2
pip install latex2sympy2==1.0.0
pip install -r requirements.txt
```

### Archivos batch disponibles
```bash
ejecutar_gui.bat                    # Ejecución normal
ejecutar_gui_compatible.bat         # Ejecución con detección de compatibilidad
instalar_dependencias_python313.bat # Instalación específica para Python 3.13
```

## Documentación

### [Guía de Usuario](README_USUARIO.md)
Instrucciones paso a paso, ejemplos prácticos y solución de problemas.

### [Documentación Técnica](README_TECNICO.md)
Especificaciones técnicas, arquitectura del sistema y detalles de implementación.

### [Documentación del Proyecto](README_PROYECTO.md)
Descripción general, casos de uso y características del proyecto.

### [Documentación del Parser](DOCUMENTACION_PARSER.md)
**Documentación especializada del componente central del sistema** - Análisis técnico profundo del InputParser, algoritmos implementados, casos límite y ejemplos de uso avanzado.

### [Instrucciones para Desarrolladores](INSTRUCCIONES_DESARROLLADOR.md)
Guía completa para desarrolladores con instrucciones de instalación, ejecución, desarrollo y solución de problemas.

## Ejemplo de Uso

**Entrada:** `\left(x^2 + 2x + 1\right)\left(x^2 - 2x + 1\right)`

**Salida:** `x^4 - 2x^2 + 1`

## Estructura del Proyecto

```
ExpaAlgebraico/
├── proyecto_expresiones/     # Código fuente principal
│   ├── giu app.py           # Interfaz gráfica
│   ├── input_parser.py      # Parser de entrada LaTeX (CORAZÓN DEL SISTEMA)
│   ├── expander.py          # Lógica de expansión
│   ├── latex_exporter.py    # Exportación a LaTeX/PDF
│   └── config.py            # Configuración y ejemplos
├── README_USUARIO.md        # Guía de usuario
├── README_TECNICO.md        # Documentación técnica
├── README_PROYECTO.md       # Documentación del proyecto
├── DOCUMENTACION_PARSER.md  # Documentación especializada del parser
└── requirements.txt         # Dependencias
```

## Casos de Uso

- **Estudiantes:** Práctica de álgebra y verificación de resultados
- **Profesores:** Preparación de material y verificación de ejercicios
- **Investigadores:** Análisis matemático y documentación

## Limitaciones

- Solo procesa **productos de factores polinómicos**
- No maneja sumas o diferencias directas
- Limitado a funciones trascendentes básicas

## Información del Autor

- **Desarrollador:** Gabriel Bustos
- **Institución:** Universidad Nacional de Colombia
- **Año:** 2025
- **Versión:** 1.0.0

## Licencia

Este proyecto es propiedad intelectual de Gabriel Bustos. Todos los derechos reservados.

---

*ExpaAlgebraico v1.0.0 - Sistema de Expansión Algebraica Profesional* 