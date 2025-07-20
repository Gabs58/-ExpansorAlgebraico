# Readme para el Desarrollador - ExpaAlgebraico

-------------------------------------------------------------------------------
-se creo un parche para evitar esto pero si no funciona en parche tener en cuenta.
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
