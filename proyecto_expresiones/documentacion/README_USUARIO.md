# ExpaAlgebraico - Guía de Usuario

## Introducción

Esta guía te ayudará a utilizar ExpaAlgebraico de manera efectiva. El sistema está diseñado para expandir expresiones algebraicas que cumplen una premisa específica: **productos de factores polinómicos convertidos a sumas de términos**.

## Inicio Rápido

### 1. Ejecutar el Sistema
```bash
# Opción 1: Usando el archivo batch
ejecutar_gui.bat

# Opción 2: Usando Python directamente
python "proyecto_expresiones/giu app.py"
```

### 2. Interfaz Principal
La GUI se divide en tres secciones principales:
- **Entrada Manual:** Donde escribes tu expresión
- **Ejemplos por Categorías:** Biblioteca de ejemplos predefinidos
- **Visualización:** Resultados expandidos en LaTeX y texto

## Uso Básico

### Paso 1: Ingresar una Expresión
1. En el campo "Expresión", escribe tu producto de factores
2. Asegúrate de que esté marcado "Entrada LaTeX: Sí"
3. Presiona "Expandir" o la tecla Enter

### Paso 2: Ver los Resultados
- **LaTeX original:** Tu expresión de entrada renderizada
- **LaTeX expandida:** El resultado expandido en notación matemática
- **Texto expandido:** El resultado en formato de texto plano
- **Resultados detallados:** Información completa del procesamiento

### Paso 3: Usar los Resultados
- **Copiar LaTeX:** Copia el resultado al portapapeles
- **Exportar a PDF:** Guarda el resultado como archivo PDF
- **Limpiar:** Borra todos los resultados

## Ejemplos Prácticos

### Ejemplo 1: Expresión Simple
**Entrada:** `(x+1)(x-1)`
**Resultado esperado:** `x^2 - 1`

**Pasos:**
1. Escribe `(x+1)(x-1)` en el campo de entrada
2. Presiona "Expandir"
3. Verifica que el resultado sea `x^2 - 1`

### Ejemplo 2: Notación LaTeX Profesional
**Entrada:** `\left(x^2 + 2x + 1\right)\left(x^2 - 2x + 1\right)`
**Resultado esperado:** `x^4 - 2x^2 + 1`

**Pasos:**
1. Escribe la expresión con `\left( ... \right)`
2. Presiona "Expandir"
3. El sistema mostrará el resultado expandido

### Ejemplo 3: Con Funciones Trigonométricas
**Entrada:** `\sin(x)(x^2 + 1)`
**Resultado esperado:** `\sin(x) \cdot x^2 + \sin(x)`

## Uso de Ejemplos Predefinidos

### Categorías Disponibles
1. **Básicos:** Expresiones simples para práctica
2. **Intermedios:** Casos con múltiples variables
3. **Avanzados:** Expresiones complejas
4. **Cheat Sheet:** Ejemplos con notación profesional

### Cómo Usar los Ejemplos
1. Selecciona una categoría del menú desplegable
2. Elige un ejemplo específico
3. El ejemplo se cargará automáticamente
4. Presiona "Expandir" para ver el resultado

## Características Avanzadas

### Sistema de Zoom
- **Zoom In (+):** Aumenta el tamaño de la interfaz
- **Zoom Out (−):** Reduce el tamaño de la interfaz
- **Ctrl + Rueda del mouse:** Zoom dinámico

### Vista Previa
- **Esquina superior derecha:** Vista previa de la entrada
- **Esquina inferior derecha:** Vista previa de la salida
- **Actualización automática:** Se actualiza al escribir

### Exportación
- **Copiar LaTeX:** Copia el resultado expandido
- **Exportar a PDF:** Requiere instalación de LaTeX
- **Formato:** LaTeX compatible con documentos académicos

## Solución de Problemas

### Error: "Por favor ingrese una expresión"
**Causa:** Campo de entrada vacío
**Solución:** Escribe una expresión válida

### Error: "Error inesperado"
**Causa:** Expresión que no cumple la premisa
**Solución:** Verifica que sea un producto de factores polinómicos

### Error: "Error al renderizar LaTeX"
**Causa:** Comandos LaTeX incompatibles
**Solución:** Usa notación estándar o consulta los ejemplos

### La GUI no se abre
**Causa:** Dependencias faltantes
**Solución:** Ejecuta `instalar_dependencias.bat`

### Error de memoria
**Causa:** Expresión demasiado compleja
**Solución:** Simplifica la expresión o divide en partes

## Consejos de Uso

### Para Estudiantes
- **Practica con ejemplos básicos** antes de expresiones complejas
- **Verifica manualmente** algunos resultados para entender el proceso
- **Usa la exportación PDF** para incluir en tareas

### Para Profesores
- **Prepara material** usando los ejemplos predefinidos
- **Exporta a PDF** para presentaciones
- **Usa la copia de LaTeX** para documentos académicos

### Para Investigadores
- **Verifica cálculos** con expresiones complejas
- **Documenta resultados** usando la exportación
- **Mantén consistencia** en notación LaTeX

## Limitaciones del Sistema

### Lo que SÍ procesa:
- Productos de factores polinómicos
- Expresiones con funciones trigonométricas básicas
- Notación LaTeX estándar
- Variables múltiples (x, y, z, etc.)

### Lo que NO procesa:
- Sumas o diferencias directas (no productos)
- Funciones trascendentes complejas
- Límites infinitos o series
- Derivadas de orden superior
- Expresiones vectoriales

## Ejemplos de Expresiones Válidas

### ✅ Expresiones Correctas
```
(x+1)(x-1)
(x^2 + y^2)(x^2 - y^2)
\sin(x)(x^2 + 1)
\left(x^3 + 1\right)\left(x^3 - 1\right)
(a+b+c)(a-b-c)
```

### ❌ Expresiones Incorrectas
```
x^2 + 2x + 1          # No es un producto
\sin(x) + \cos(x)     # No es un producto
\int f(x) dx          # No es un producto
\lim_{x \to 0} f(x)   # No es un producto
```

## Comandos de Línea

### Modo CLI
```bash
python proyecto_expresiones/main.py "expresión"
```

### Ejemplos CLI
```bash
python main.py "(x+1)(x-1)"
python main.py "\sin(x)(x^2+1)"
```

## Configuración Avanzada

### Variables de Entorno
- `PYTHONPATH`: Configuración de módulos
- `LATEX_PATH`: Ruta a instalación LaTeX

### Archivos de Configuración
- `config.py`: Ejemplos y categorías
- `requirements.txt`: Dependencias

## Soporte Técnico

### Información del Sistema
- **Versión:** 1.0.0
- **Autor:** Gabriel Bustos
- **Institución:** Universidad Nacional de Colombia

### Recursos Adicionales
- **README_TECNICO.md:** Documentación técnica detallada
- **README_PROYECTO.md:** Información general del proyecto
- **Ejemplos en GUI:** Biblioteca completa de casos

### Contacto
Para reportar problemas o solicitar mejoras:
1. Verifica que el problema cumple la premisa del sistema
2. Incluye la expresión exacta que causa el error
3. Describe el comportamiento esperado

---

*Guía de usuario para ExpaAlgebraico v1.0.0 - Desarrollado por Gabriel Bustos* 

## Novedades y Mejoras Recientes (Junio 2024)

- El sistema ahora soporta correctamente expresiones avanzadas en notación LaTeX: sumatorias, integrales, derivadas, funciones trigonométricas y binomios a potencia.
- Se implementó un parser robusto que identifica el tipo de expresión y aplica reglas de reescritura y parsing específicas, garantizando resultados correctos incluso en casos límite.
- El sistema nunca muestra errores técnicos al usuario: siempre entrega un resultado válido o una sugerencia clara.
- Cobertura total en pruebas: 100% de éxito en todas las categorías, incluyendo casos extremos y expresiones anidadas.

### Ejemplos de Expresiones Avanzadas Ahora Soportadas

| Entrada LaTeX | Salida Expandida |
|--------------|------------------|
| `\sum_{n=1}^{5} (n+1)(n-1)` | `\sum_{n=1}^{5} (n^2 - 1)` |
| `\int_0^1 (x^2+1)(x-1) dx` | `\int_0^1 (x^3 - x^2 + x - 1) dx` |
| `\frac{d}{dx}[(x^2+1)(x-1)]` | `\frac{d}{dx}[x^3 - x^2 + x - 1]` |
| `\sin(x)(x^2+1)` | `\sin(x) \cdot x^2 + \sin(x)` |

--- 