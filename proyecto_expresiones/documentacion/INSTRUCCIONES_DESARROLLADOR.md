# Instrucciones para el Desarrollador - ExpaAlgebraico

-------------------------------------------------------------------------------

## IMPORTANTE PARA TODOS LOS USUARIOS DE PYTHON

Antes de ejecutar la GUI o cualquier script, asegúrese de que:

- Está usando el intérprete de Python correcto (el mismo donde instaló las dependencias).
- Si tiene varios Python instalados (por ejemplo, 3.12 y 3.13, o entornos virtuales), verifique cuál está activo.
- Instale siempre las dependencias con:
  ```sh
  python -m pip install -r requirements.txt
  ```
  o, para una dependencia específica:
  ```sh
  python -m pip install latex2sympy2
  ```
- Si usa un entorno virtual, actívelo antes de instalar dependencias o ejecutar la GUI.

Nota: Si no sigue estos pasos, puede recibir errores como “No module named ...” aunque ya haya instalado la librería.

-------------------------------------------------------------------------------

## IMPORTANTE PARA USUARIOS DE VISUAL STUDIO CODE

ATENCIÓN: Si utiliza Visual Studio Code, es imprescindible seleccionar el intérprete de Python correcto y asegurarse de instalar las librerías en ese entorno. Si no lo hace, la GUI no funcionará y aparecerán errores como "latex2sympy2 no está disponible".

Lea y siga los pasos de la sección "¡Importante para usuarios de Visual Studio Code!" antes de ejecutar la GUI.

-------------------------------------------------------------------------------

## Lista de verificación antes de ejecutar la GUI

- [ ] Seleccioné el intérprete de Python correcto en Visual Studio Code
- [ ] Instalé las dependencias usando `python -m pip install ...` en la terminal de Visual Studio Code
- [ ] (Opcional) Reinicié Visual Studio Code después de instalar dependencias

-------------------------------------------------------------------------------

## ¡Importante para usuarios de Visual Studio Code!

Si ejecuta la GUI desde Visual Studio Code y observa errores como:

    Error al procesar la expresión: latex2sympy2 no está disponible. Instala con: pip install latex2sympy2

Probablemente está utilizando un intérprete de Python diferente al que tiene instaladas las librerías.

### ¿Cómo evitarlo?

1. Seleccione el intérprete correcto en Visual Studio Code:
   - Haga clic en la barra inferior izquierda (o superior derecha) donde aparece la versión de Python.
   - Elija el intérprete donde instaló las dependencias (puede ser un entorno virtual o su Python principal).

2. Instale las librerías en ese intérprete:
   - Abra la terminal integrada de Visual Studio Code.
   - Ejecute:
     ```sh
     python -m pip install latex2sympy2
     ```
   - Esto asegura que la librería se instala en el mismo Python que usará la GUI.

3. Reinicie Visual Studio Code después de cambiar el intérprete o instalar nuevas librerías.

4. Ejecute la GUI desde Visual Studio Code usando el botón de "Run" o el comando:
   ```sh
   python "proyecto_expresiones/giu app.py"
   ```

Nota: Si tiene varios Python o utiliza un entorno virtual, siempre verifique que el intérprete seleccionado sea el correcto.

-------------------------------------------------------------------------------

## Requisito Adicional: Instalación de MiKTeX

Para que el sistema pueda exportar resultados a PDF y renderizar correctamente expresiones LaTeX, es necesario instalar una distribución LaTeX. Se recomienda instalar MiKTeX:

1. Descargue MiKTeX desde: https://miktex.org/download
2. Ejecute el instalador y acepte las condiciones de copia (como se muestra en la imagen a continuación).
3. Complete la instalación con la configuración por defecto.

![Pantalla de aceptación de MiKTeX](doc/img/miktex_accept.png)

Nota: Si MiKTeX no está instalado, la exportación a PDF y el renderizado avanzado de LaTeX no funcionarán correctamente.

## Documentación Técnica Avanzada

Para detalles sobre la arquitectura, dependencias, integración de LaTeX y funcionamiento interno, consulte el archivo:
- [`README_TECNICO.md`](README_TECNICO.md)

## Opciones de Ejecución

### Opción 1: Ejecución Automática (Recomendada)
1. Ejecutar `ejecutar_gui_compatible.bat`
2. El sistema detectará automáticamente la versión de Python y aplicará las correcciones necesarias

### Opción 2: Python 3.12 (Más Estable)
Si tiene Python 3.12 instalado:
1. Ejecutar `ejecutar_gui.bat`
2. El sistema funcionará sin problemas de compatibilidad

### Opción 3: Python 3.13 (Con Correcciones)
Si tiene Python 3.13:
1. Ejecutar `instalar_dependencias_python313.bat`
2. Esperar a que termine la instalación
3. Ejecutar `ejecutar_gui.bat`

## Verificación de Funcionamiento

El sistema mostrará una interfaz gráfica con:
- Campo de entrada para expresiones LaTeX
- Botón "Expandir" para procesar la expresión
- Área de visualización con el resultado
- Biblioteca de ejemplos predefinidos

Sugerencia: Puede agregar aquí una captura de pantalla de la GUI funcionando para mayor claridad. Por ejemplo:

![GUI funcionando](doc/img/gui_ok.png)

## Ejemplo de Prueba

1. En el campo de entrada, escribir: `(x+1)(x-1)`
2. Hacer clic en "Expandir"
3. El resultado debería ser: `x^2 - 1`

## Desarrollo y Modificación

### Estructura del Código
- `proyecto_expresiones/giu app.py` - Interfaz gráfica principal
- `proyecto_expresiones/input_parser.py` - Parser de entrada (componente central)
- `proyecto_expresiones/expander.py` - Lógica de expansión algebraica
- `proyecto_expresiones/latex_exporter.py` - Exportación a LaTeX/PDF
- `proyecto_expresiones/config.py` - Configuración y ejemplos

### Modificaciones Recomendadas
- Para agregar nuevas funcionalidades: modificar `expander.py`
- Para cambiar la interfaz: modificar `giu app.py`
- Para ajustar el parsing: modificar `input_parser.py`
- Para nuevos ejemplos: modificar `config.py`

## Solución de Problemas

### Error: "No module named 'typing.io'"
- Ejecutar `instalar_dependencias_python313.bat`
- O instalar Python 3.12 desde python.org

### Error: "ModuleNotFoundError"
- Ejecutar `instalar_dependencias_python313.bat`
- Verificar que Python esté en el PATH del sistema

### La GUI no se abre
- Verificar que todas las dependencias estén instaladas
- Usar `ejecutar_gui_compatible.bat` para diagnóstico automático

### Problemas de Rendimiento
- Verificar que matplotlib esté configurado correctamente
- Revisar la configuración de LaTeX en `latex_exporter.py`

## Características del Sistema

- Especialización: Expansión de productos de factores polinómicos
- Entrada: Notación LaTeX
- Salida: Expresiones expandidas en LaTeX
- Interfaz: Gráfica intuitiva con ejemplos incluidos
- Exportación: Capacidad de generar PDF con resultados

## Información Técnica

- Desarrollador: Gabriel Bustos
- Lenguaje: Python 3.12/3.13
- Bibliotecas principales: SymPy, LaTeX2SymPy2, Matplotlib, PIL
- Arquitectura: Modular con parser especializado

## Contacto

Para cualquier problema técnico o consulta sobre el funcionamiento, contactar al desarrollador: 
gbustosm@unal.edu.co

---

Sistema de Expansión Algebraica - Versión 1.0.0 
