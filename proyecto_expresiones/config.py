# ExpaAlgebraico v1.0.0 - Desarrollado por Gabriel Bustos (Universidad Nacional de Colombia, 2025)
# Configuración centralizada del sistema con ejemplos organizados por categorías
#
# NOTA IMPORTANTE:
# - Los ejemplos LaTeX se dividen en dos grupos:
#   1. NO-EXTREMOS (<1200 caracteres): recomendados, funcionan bien con el parser y la GUI.
#   2. EXTREMOS (>=1200 caracteres): NO soportados por el parser, la GUI lo advertirlo.
# - El diccionario CATEGORIAS_EJEMPLOS solo contiene ejemplos no-extremos.
# - El diccionario CATEGORIAS_EJEMPLOS_EXTREMOS contiene los extremos.

# Ejemplos básicos de productos de binomios
EJEMPLOS_BASICOS = [
    r"(x+1)(x-1)",
    r"(x^{2}+1)(x-1)",
    r"(x+y)(x-y)",
    r"(a+b)(a-b)",
    r"(x^{2}+2x+1)(x-1)",
    r"(x^{2}+2x+1)(x^{2}-2x+1)",
    r"(x^{3}+1)(x^{3}-1)",
    r"(x^{2}+xy+y^{2})(x^{2}-xy+y^{2})"
]

# Ejemplos con productos de binomios y trinomios 
EJEMPLOS_PRODUCTOS_BINOMIOS = [
    r"(x+1)(x-1)",
    r"(x^{2}+1)(x-1)",
    r"(x+y)(x-y)",
    r"(a+b)(a-b)",
    r"(x+1)(x^{2}+1)",
    r"(x+y+z)(x-y-z)"
]

# Ejemplos con productos de polinomios y potencias 
EJEMPLOS_PRODUCTOS_POTENCIAS = [
    r"(x+1)^{2}(x-1)",
    r"(x+y)^{2}(x-y)",
    r"(x^{2}+1)^{2}(x^{2}-1)",
    r"(x+1)^{3}(x-1)",
    r"(x^{2}+2x+1)(x^{2}-2x+1)",
    r"(x^{3}+1)(x^{3}-1)"
]

# Ejemplos con sumatorias de productos 
EJEMPLOS_SUMATORIAS = [
    r"\sum_{n=1}^{5} (n+1)(n-1)",
    r"\sum_{k=0}^{m} (k^{2}+1)(k-1)",
    r"\sum_{i=1}^{n} (i+2)(i-2)",
    r"\sum_{j=1}^{10} (j^{2}+1)(j-1)",
    r"\sum_{p=1}^{4} (p^{3}+1)(p-1)"
]

# Ejemplos con integrales de productos 
EJEMPLOS_INTEGRALES = [
    r"\int (x+1)(x-1) dx",
    r"\int (x^{2}+1)(x-1) dx",
    r"\int (x+2)(x-2) dx",
    r"\int (x^{3}+1)(x-1) dx",
    r"\int (x+y)(x-y) dx"
]

# Multiplicatorias (Productorias)
MULTIPLICATORIAS = [
    r"\prod_{n=1}^{5} (n+1)(n-1)",
    r"\prod_{i=1}^{3} (i+2)(i-2)",
    r"\prod_{k=1}^{n} (k+1)(k-1)",
    r"\prod_{j=1}^{4} (j^2+1)(j-1)",
    r"\prod_{m=1}^{2} (m+3)(m-3)"
]

# Ejemplos con derivadas simples de productos 
EJEMPLOS_DERIVADAS = [
    r"\frac{d}{dx}[(x+1)(x-1)]",
    r"\frac{d}{dx}[(x^{2}+1)(x-1)]",
    r"\frac{d}{dx}[(x+2)(x-2)]",
    r"\frac{d}{dx}[(x^{3}+1)(x-1)]",
    r"\frac{d}{dx}[(x+y)(x-y)]"
]

# Ejemplos con productos de polinomios más complejos
EJEMPLOS_POLINOMIOS_COMPLEJOS = [
    r"(x^{3}+2x^{2}+x+1)(x^{2}-3x+2)",
    r"(x^{4}+1)(x^{2}+1)(x+1)",
    r"(x^{3}-1)(x^{3}+1)(x^{2}+1)",
    r"(x^{2}+xy+y^{2})(x^{2}-xy+y^{2})",
    r"(x^{3}+3x^{2}+3x+1)(x^{3}-3x^{2}+3x-1)",
    r"(x^{4}+4x^{3}+6x^{2}+4x+1)(x-1)"
]

# Ejemplos con productos de polinomios cuadráticos
EJEMPLOS_PRODUCTOS_CUADRATICOS = [
    r"(x^{2}+1)(x^{2}-1)",
    r"(x^{2}+2x+1)(x^{2}-2x+1)",
    r"(x^{2}+xy+y^{2})(x^{2}-xy+y^{2})",
    r"(x^{2}+3x+2)(x^{2}-3x+2)",
    r"(x^{2}+4x+4)(x^{2}-4x+4)",
    r"(x^{2}+6x+9)(x^{2}-6x+9)"
]

# Ejemplos con productos de polinomios cúbicos
EJEMPLOS_PRODUCTOS_CUBICOS = [
    r"(x^{3}+1)(x^{3}-1)",
    r"(x^{3}+2x^{2}+x+1)(x^{3}-2x^{2}+x-1)",
    r"(x^{3}+3x^{2}+3x+1)(x^{3}-3x^{2}+3x-1)",
    r"(x^{3}+x^{2}+x+1)(x^{3}-x^{2}+x-1)",
    r"(x^{3}+4x^{2}+5x+2)(x^{3}-4x^{2}+5x-2)",
    r"(x^{3}+5x^{2}+7x+3)(x^{3}-5x^{2}+7x-3)"
]

# Ejemplos con productos de binomios elevados a potencias
EJEMPLOS_BINOMIOS_POTENCIAS = [
    r"(x+1)^{2}(x-1)^{2}",
    r"(x+1)^{3}(x-1)^{3}",
    r"(x+y)^{2}(x-y)^{2}",
    r"(x+1)^{4}(x-1)^{4}",
    r"(x^{2}+1)^{2}(x^{2}-1)^{2}",
    r"(x+1)^{5}(x-1)^{5}"
]

# Ejemplos con productos de trinomios
EJEMPLOS_TRINOMIOS = [
    r"(x^{2}+2x+1)(x^{2}-2x+1)",
    r"(x^{2}+3x+2)(x^{2}-3x+2)",
    r"(x^{2}+xy+y^{2})(x^{2}-xy+y^{2})",
    r"(x^{2}+2xy+y^{2})(x^{2}-2xy+y^{2})",
    r"(x^{2}+4x+4)(x^{2}-4x+4)",
    r"(x^{2}+6x+9)(x^{2}-6x+9)"
]

# Ejemplos con productos de polinomios de grado superior
EJEMPLOS_POLINOMIOS_SUPERIORES = [
    r"(x^{5}+1)(x^{5}-1)",
    r"(x^{6}+1)(x^{6}-1)",
    r"(x^{4}+2x^{2}+1)(x^{4}-2x^{2}+1)",
    r"(x^{5}+5x^{4}+10x^{3}+10x^{2}+5x+1)(x-1)",
    r"(x^{6}+6x^{5}+15x^{4}+20x^{3}+15x^{2}+6x+1)(x-1)",
    r"(x^{4}+4x^{3}+6x^{2}+4x+1)(x^{4}-4x^{3}+6x^{2}-4x+1)"
]

# Ejemplos con productos de expresiones con múltiples variables
EJEMPLOS_MULTIPLES_VARIABLES = [
    r"(x+y+z)(x-y-z)",
    r"(x+y+z)(x+y-z)(x-y+z)",
    r"(x^{2}+y^{2}+z^{2})(x^{2}-y^{2}-z^{2})",
    r"(x+y+z)^{2}(x-y-z)^{2}",
    r"(x^{2}+xy+y^{2})(x^{2}-xy+y^{2})(x^{2}+xz+z^{2})",
    r"(x+y+z)(x-y-z)(x-y+z)(x+y-z)"
]

# Ejemplos con productos de expresiones con coeficientes
EJEMPLOS_COEFICIENTES = [
    r"(2x+1)(2x-1)",
    r"(3x+2)(3x-2)(3x+1)",
    r"(5x^{2}+3x+1)(5x^{2}-3x+1)",
    r"(7x+4)(7x-4)(7x+2)(7x-2)",
    r"(11x^{3}+5x^{2}+3x+1)(11x^{3}-5x^{2}+3x-1)",
    r"(13x^{2}+7x+3)(13x^{2}-7x+3)(13x^{2}+5x+2)"
]

# Ejemplos con productos de polinomios de grado alto
EJEMPLOS_POLINOMIOS_GRADO_ALTO = [
    r"(x^{4}+1)(x^{4}-1)(x^{2}+1)",
    r"(x^{5}+1)(x^{5}-1)(x^{3}+1)",
    r"(x^{6}+1)(x^{6}-1)(x^{4}+1)",
    r"(x^{7}+1)(x^{7}-1)(x^{5}+1)",
    r"(x^{8}+1)(x^{8}-1)(x^{6}+1)",
    r"(x^{9}+1)(x^{9}-1)(x^{7}+1)"
]

# Ejemplos con coeficientes fraccionarios y negativos
EJEMPLOS_COEFICIENTES_FRACCIONARIOS = [
    r"(2x-3)(x+1)",
    r"(-x+2)(x-5)",
    r"\left(\frac{1}{2}x+1\right)\left(x-2\right)",
    r"\left(-\frac{3}{4}x+2\right)\left(x+4\right)",
    r"(5x-\frac{1}{3})(x+\frac{2}{5})",
    r"(x-1)(-2x+3)",
    r"\left(\frac{3}{7}x-1\right)(x+5)",
    r"\left(\frac{\sqrt{2}}{3}x+\frac{1}{4}\right)\left(x-\frac{\pi}{2}\right)",
    r"\left(\frac{-5}{8}x^2+\frac{3}{4}x-\frac{1}{6}\right)\left(x+\frac{2}{3}\right)",
    r"\left(\frac{a}{b}x+\frac{c}{d}\right)\left(\frac{p}{q}x-\frac{r}{s}\right)"
]

# Ejemplos con subíndices y superíndices
EJEMPLOS_SUBINDICES_SUPERINDICES = [
    r"(x_{1}+x_{2})(x_{1}-x_{2})",
    r"(y_{1}^{2}+y_{2}^{2})(y_{1}^{2}-y_{2}^{2})",
    r"(a_{1}^{2}+b_{2}^{2})(a_{1}^{2}-b_{2}^{2})",
    r"(z_{3}+z_{4})(z_{3}-z_{4})",
    r"(w_{1}^{3}+w_{2}^{3})(w_{1}^{3}-w_{2}^{3})",
    r"(x_{i}+y_{j})(x_{i}-y_{j})"
]

# Ejemplos con letras mayúsculas y minúsculas
EJEMPLOS_MAYUSCULAS_MINUSCULAS = [
    r"(X+Y)(X-Y)",
    r"(A+B+C)(A-B+C)",
    r"(M^{2}+N^{2})(M^{2}-N^{2})",
    r"(P+Q+R)(P-Q+R)",
    r"(X^{2}+2XY+Y^{2})(X^{2}-2XY+Y^{2})",
    r"(a+b)(A+B)"
]

# Ejemplos con variables distintas
EJEMPLOS_VARIABLES_DISTINTAS = [
    r"(x+y)(a+b)",
    r"(m+n)(p+q)",
    r"(u+v+w)(s+t)",
    r"(x_{1}+y_{2})(a_{1}+b_{2})",
    r"(x^{2}+y^{2})(a^{2}+b^{2})",
    r"(x+y+z)(a+b+c)"
]

# Ejemplos con funciones trigonométricas
EJEMPLOS_TRIGONOMETRICOS = [
    r"(\sin{x}+\cos{x})(\sin{x}-\cos{x})",
    r"(\sin^{2}{x}+1)(\sin{x}-1)",
    r"(\cos{x}+1)(\cos{x}-1)",
    r"(\tan{x}+1)(\tan{x}-1)",
    r"(\sin{x}+\cos{x})^{2}(\sin{x}-\cos{x})",
    r"(\sin{x}+1)(\sin{x}-1)(\cos{x}+1)",
    r"(\sin^{2}{x}+\cos^{2}{x})(\sin{x}-\cos{x})",
    r"(\sin{x}+\cos{x})(\sin{x}+\cos{x})(\sin{x}-\cos{x})",
    r"(\sin{2x}+\cos{2x})(\sin{2x}-\cos{2x})",
    r"(\sin{\theta}+\cos{\theta})(\sin{\theta}-\cos{\theta})"
]

# Ejemplos con integrales de funciones trigonométricas
EJEMPLOS_INTEGRALES_TRIGONOMETRICAS = [
    r"\int (\sin{x}+\cos{x})(\sin{x}-\cos{x}) dx",
    r"\int (\sin^{2}{x}+1)(\sin{x}-1) dx",
    r"\int (\cos{x}+1)(\cos{x}-1) dx",
    r"\int (\sin{x}+\cos{x})^{2}(\sin{x}-\cos{x}) dx",
    r"\int_{0}^{\pi} (\sin{x}+\cos{x})(\sin{x}-\cos{x}) dx"
]

# Ejemplos con derivadas de funciones trigonométricas
EJEMPLOS_DERIVADAS_TRIGONOMETRICAS = [
    r"\frac{d}{dx}[(\sin{x}+\cos{x})(\sin{x}-\cos{x})]",
    r"\frac{d}{dx}[(\sin^{2}{x}+1)(\sin{x}-1)]",
    r"\frac{d}{dx}[(\cos{x}+1)(\cos{x}-1)]",
    r"\frac{d}{dx}[(\sin{x}+\cos{x})^{2}(\sin{x}-\cos{x})]",
    r"\frac{d^{2}}{dx^{2}}[(\sin{x}+\cos{x})(\sin{x}-\cos{x})]"
]

# Ejemplos con sumatorias de funciones trigonométricas
EJEMPLOS_SUMATORIAS_TRIGONOMETRICAS = [
    r"\sum_{n=1}^{3} (\sin{n\theta}+\cos{n\theta})(\sin{n\theta}-\cos{n\theta})",
    r"\sum_{k=0}^{2} (\sin^{2}{k\pi}+1)(\sin{k\pi}-1)",
    r"\sum_{i=1}^{4} (\cos{i\alpha}+1)(\cos{i\alpha}-1)",
    r"\sum_{j=1}^{3} (\sin{j\beta}+\cos{j\beta})^{2}(\sin{j\beta}-\cos{j\beta})"
]

# Ejemplos con productos de funciones trigonométricas
EJEMPLOS_PRODUCTOS_TRIGONOMETRICOS = [
    r"\prod_{n=1}^{2} (\sin{n\theta}+\cos{n\theta})(\sin{n\theta}-\cos{n\theta})",
    r"\prod_{k=1}^{3} (\sin^{2}{k\pi}+1)(\sin{k\pi}-1)",
    r"\prod_{i=1}^{2} (\cos{i\alpha}+1)(\cos{i\alpha}-1)",
    r"\prod_{j=1}^{2} (\sin{j\beta}+\cos{j\beta})^{2}(\sin{j\beta}-\cos{j\beta})"
]

# CASOS LÍMITE - Productos de factores polinómicos complejos
EJEMPLOS_CASOS_LIMITE_POLINOMIOS = [
    "(x^7+7x^6+21x^5+35x^4+35x^3+21x^2+7x+1)(x^7-7x^6+21x^5-35x^4+35x^3-21x^2+7x-1)",
    "(x^8+8x^7+28x^6+56x^5+70x^4+56x^3+28x^2+8x+1)(x^8-8x^7+28x^6-56x^5+70x^4-56x^3+28x^2-8x+1)",
    "(x^9+9x^8+36x^7+84x^6+126x^5+126x^4+84x^3+36x^2+9x+1)(x^9-9x^8+36x^7-84x^6+126x^5-126x^4+84x^3-36x^2+9x-1)",
    "(x^{10}+10x^9+45x^8+120x^7+210x^6+252x^5+210x^4+120x^3+45x^2+10x+1)(x^{10}-10x^9+45x^8-120x^7+210x^6-252x^5+210x^4-120x^3+45x^2-10x+1)",
    "(x^{12}+12x^{11}+66x^{10}+220x^9+495x^8+792x^7+924x^6+792x^5+495x^4+220x^3+66x^2+12x+1)(x^{12}-12x^{11}+66x^{10}-220x^9+495x^8-792x^7+924x^6-792x^5+495x^4-220x^3+66x^2-12x+1)",
    "(x^{15}+15x^{14}+105x^{13}+455x^{12}+1365x^{11}+3003x^{10}+5005x^9+6435x^8+6435x^7+5005x^6+3003x^5+1365x^4+455x^3+105x^2+15x+1)(x^{15}-15x^{14}+105x^{13}-455x^{12}+1365x^{11}-3003x^{10}+5005x^9-6435x^8+6435x^7-5005x^6+3003x^5-1365x^4+455x^3-105x^2+15x-1)"
]

# CASOS LÍMITE - Productos de polinomios de grado alto 
EJEMPLOS_CASOS_LIMITE_POLINOMIOS_ALTOS = [
    "(x^5+5x^4+10x^3+10x^2+5x+1)(x^5-5x^4+10x^3-10x^2+5x-1)(x^3+1)",
    "(x^6+6x^5+15x^4+20x^3+15x^2+6x+1)(x^6-6x^5+15x^4-20x^3+15x^2-6x+1)(x^4+1)",
    "(x^7+7x^6+21x^5+35x^4+35x^3+21x^2+7x+1)(x^7-7x^6+21x^5-35x^4+35x^3-21x^2+7x-1)(x^5+1)",
    "(x^8+8x^7+28x^6+56x^5+70x^4+56x^3+28x^2+8x+1)(x^8-8x^7+28x^6-56x^5+70x^4-56x^3+28x^2-8x+1)(x^6+1)",
    "(x^9+9x^8+36x^7+84x^6+126x^5+126x^4+84x^3+36x^2+9x+1)(x^9-9x^8+36x^7-84x^6+126x^5-126x^4+84x^3-36x^2+9x-1)(x^7+1)",
    "(x^{10}+10x^9+45x^8+120x^7+210x^6+252x^5+210x^4+120x^3+45x^2+10x+1)(x^{10}-10x^9+45x^8-120x^7+210x^6-252x^5+210x^4-120x^3+45x^2-10x+1)(x^8+1)"
]

# CASOS LÍMITE - Productos de sumatorias complejas
EJEMPLOS_CASOS_LIMITE_SUMATORIAS = [
    r"\sum_{n=1}^{10} (n^5+5n^4+10n^3+10n^2+5n+1)(n^5-5n^4+10n^3-10n^2+5n-1)",
    r"\sum_{k=0}^{15} (k^6+6k^5+15k^4+20k^3+15k^2+6k+1)(k^6-6k^5+15k^4-20k^3+15k^2-6k+1)",
    r"\sum_{i=1}^{20} (i^7+7i^6+21i^5+35i^4+35i^3+21i^2+7i+1)(i^7-7i^6+21i^5-35i^4+35i^3-21i^2+7i-1)",
    r"\sum_{j=0}^{25} (j^8+8j^7+28j^6+56j^5+70j^4+56j^3+28j^2+8j+1)(j^8-8j^7+28j^6-56j^5+70j^4-56j^3+28j^2-8j+1)",
    r"\sum_{m=1}^{30} (m^9+9m^8+36m^7+84m^6+126m^5+126m^4+84m^3+36m^2+9m+1)(m^9-9m^8+36m^7-84m^6+126m^5-126m^4+84m^3-36m^2+9m-1)",
    r"\sum_{p=0}^{35} (p^{10}+10p^9+45p^8+120p^7+210p^6+252p^5+210p^4+120p^3+45p^2+10p+1)(p^{10}-10p^9+45p^8-120p^7+210p^6-252p^5+210p^4-120p^3+45p^2-10p+1)"
]

# CASOS LÍMITE - Productos de integrales complejas
EJEMPLOS_CASOS_LIMITE_INTEGRALES = [
    r"\int_0^1 (x^5+5x^4+10x^3+10x^2+5x+1)(x^5-5x^4+10x^3-10x^2+5x-1) dx",
    r"\int_{0}^{2} (x^6+6x^5+15x^4+20x^3+15x^2+6x+1)(x^6-6x^5+15x^4-20x^3+15x^2-6x+1) dx",
    r"\int_{-1}^{1} (x^7+7x^6+21x^5+35x^4+35x^3+21x^2+7x+1)(x^7-7x^6+21x^5-35x^4+35x^3-21x^2+7x-1) dx",
    r"\int_{0}^{\pi} (x^8+8x^7+28x^6+56x^5+70x^4+56x^3+28x^2+8x+1)(x^8-8x^7+28x^6-56x^5+70x^4-56x^3+28x^2-8x+1) dx",
    r"\int_{-\infty}^{\infty} (x^9+9x^8+36x^7+84x^6+126x^5+126x^4+84x^3+36x^2+9x+1)(x^9-9x^8+36x^7-84x^6+126x^5-126x^4+84x^3-36x^2+9x-1) e^{-x^2} dx",
    r"\int_{0}^{1} (x^{10}+10x^9+45x^8+120x^7+210x^6+252x^5+210x^4+120x^3+45x^2+10x+1)(x^{10}-10x^9+45x^8-120x^7+210x^6-252x^5+210x^4-120x^3+45x^2-10x+1) dx"
]

# CASOS LÍMITE - Productos de derivadas complejas
EJEMPLOS_CASOS_LIMITE_DERIVADAS = [
    r"\frac{d}{dx}[(x^5+5x^4+10x^3+10x^2+5x+1)(x^5-5x^4+10x^3-10x^2+5x-1)]",
    r"\frac{d}{dx}[(x^6+6x^5+15x^4+20x^3+15x^2+6x+1)(x^6-6x^5+15x^4-20x^3+15x^2-6x+1)]",
    r"\frac{d}{dx}[(x^7+7x^6+21x^5+35x^4+35x^3+21x^2+7x+1)(x^7-7x^6+21x^5-35x^4+35x^3-21x^2+7x-1)]",
    r"\frac{d}{dx}[(x^8+8x^7+28x^6+56x^5+70x^4+56x^3+28x^2+8x+1)(x^8-8x^7+28x^6-56x^5+70x^4-56x^3+28x^2-8x+1)]",
    r"\frac{d}{dx}[(x^9+9x^8+36x^7+84x^6+126x^5+126x^4+84x^3+36x^2+9x+1)(x^9-9x^8+36x^7-84x^6+126x^5-126x^4+84x^3-36x^2+9x-1)]",
    r"\frac{d}{dx}[(x^{10}+10x^9+45x^8+120x^7+210x^6+252x^5+210x^4+120x^3+45x^2+10x+1)(x^{10}-10x^9+45x^8-120x^7+210x^6-252x^5+210x^4-120x^3+45x^2-10x+1)]"
]

# CASOS LÍMITE - Productos de expresiones con múltiples variables complejas
EJEMPLOS_CASOS_LIMITE_MULTIVARIABLES = [
    "(x^3+y^3+z^3+3x^2y+3x^2z+3xy^2+3xz^2+3y^2z+3yz^2+6xyz)(x^3+y^3+z^3-3x^2y-3x^2z-3xy^2-3xz^2-3y^2z-3yz^2+6xyz)",
    "(x^4+y^4+z^4+w^4+4x^3y+4x^3z+4x^3w+4xy^3+4xz^3+4xw^3+4y^3z+4y^3w+4z^3w+6x^2y^2+6x^2z^2+6x^2w^2+6y^2z^2+6y^2w^2+6z^2w^2+12x^2yz+12x^2yw+12x^2zw+12xy^2z+12xy^2w+12xz^2y+12xz^2w+12xw^2y+12xw^2z+12y^2zw+12yz^2w+12yzw^2+24xyzw)(x^4+y^4+z^4+w^4-4x^3y-4x^3z-4x^3w-4xy^3-4xz^3-4xw^3-4y^3z-4y^3w-4z^3w+6x^2y^2+6x^2z^2+6x^2w^2+6y^2z^2+6y^2w^2+6z^2w^2-12x^2yz-12x^2yw-12x^2zw-12xy^2z-12xy^2w-12xz^2y-12xz^2w-12xw^2y-12xw^2z-12y^2zw-12yz^2w-12yzw^2+24xyzw)",
    "(x^5+y^5+z^5+5x^4y+5x^4z+5xy^4+5xz^4+5y^4z+5yz^4+10x^3y^2+10x^3z^2+10x^2y^3+10x^2z^3+10y^3z^2+10y^2z^3+20x^3yz+20xy^3z+20xyz^3+30x^2y^2z+30x^2yz^2+30xy^2z^2)(x^5+y^5+z^5-5x^4y-5x^4z-5xy^4-5xz^4-5y^4z-5yz^4+10x^3y^2+10x^3z^2+10x^2y^3+10x^2z^3+10y^3z^2+10y^2z^3-20x^3yz-20xy^3z-20xyz^3+30x^2y^2z+30x^2yz^2+30xy^2z^2)",
    "(x^6+y^6+z^6+6x^5y+6x^5z+6xy^5+6xz^5+6y^5z+6yz^5+15x^4y^2+15x^4z^2+15x^2y^4+15x^2z^4+15y^4z^2+15y^2z^4+20x^3y^3+20x^3z^3+20y^3z^3+30x^4yz+30xy^4z+30xyz^4+60x^3y^2z+60x^3yz^2+60x^2y^3z+60x^2yz^3+60xy^3z^2+60xy^2z^3+90x^2y^2z^2)(x^6+y^6+z^6-6x^5y-6x^5z-6xy^5-6xz^5-6y^5z-6yz^5+15x^4y^2+15x^4z^2+15x^2y^4+15x^2z^4+15y^4z^2+15y^2z^4+20x^3y^3+20x^3z^3+20y^3z^3-30x^4yz-30xy^4z-30xyz^4+60x^3y^2z+60x^3yz^2+60x^2y^3z+60x^2yz^3+60xy^3z^2+60xy^2z^3-90x^2y^2z^2)",
    "(x^7+y^7+z^7+7x^6y+7x^6z+7xy^6+7xz^6+7y^6z+7yz^6+21x^5y^2+21x^5z^2+21x^2y^5+21x^2z^5+21y^5z^2+21y^2z^5+35x^4y^3+35x^4z^3+35x^3y^4+35x^3z^4+35y^4z^3+35y^3z^4+42x^5yz+42xy^5z+42xyz^5+105x^4y^2z+105x^4yz^2+105x^2y^4z+105x^2yz^4+105xy^4z^2+105xy^2z^4+140x^3y^3z+140x^3yz^3+140xy^3z^3+210x^3y^2z^2+210x^2y^3z^2+210x^2y^2z^3)(x^7+y^7+z^7-7x^6y-7x^6z-7xy^6-7xz^6-7y^6z-7yz^6+21x^5y^2+21x^5z^2+21x^2y^5+21x^2z^5+21y^5z^2+21y^2z^5+35x^4y^3+35x^4z^3+35x^3y^4+35x^3z^4+35y^4z^3+35y^3z^4-42x^5yz-42xy^5z-42xyz^5+105x^4y^2z+105x^4yz^2+105x^2y^4z+105x^2yz^4+105xy^4z^2+105xy^2z^4+140x^3y^3z+140x^3yz^3+140xy^3z^3-210x^3y^2z^2-210x^2y^3z^2-210x^2y^2z^3)",
    "(x^8+y^8+z^8+8x^7y+8x^7z+8xy^7+8xz^7+8y^7z+8yz^7+28x^6y^2+28x^6z^2+28x^2y^6+28x^2z^6+28y^6z^2+28y^2z^6+56x^5y^3+56x^5z^3+56x^3y^5+56x^3z^5+56y^5z^3+56y^3z^5+70x^4y^4+70x^4z^4+70y^4z^4+56x^6yz+56xy^6z+56xyz^6+168x^5y^2z+168x^5yz^2+168x^2y^5z+168x^2yz^5+168xy^5z^2+168xy^2z^5+280x^4y^3z+280x^4yz^3+280x^3y^4z+280x^3yz^4+280xy^4z^3+280xy^3z^4+420x^4y^2z^2+420x^2y^4z^2+420x^2y^2z^4+560x^3y^3z^2+560x^3y^2z^3+560x^2y^3z^3)(x^8+y^8+z^8-8x^7y-8x^7z-8xy^7-8xz^7-8y^7z-8yz^7+28x^6y^2+28x^6z^2+28x^2y^6+28x^2z^6+28y^6z^2+28y^2z^6+56x^5y^3+56x^5z^3+56x^3y^5+56x^3z^5+56y^5z^3+56y^3z^5+70x^4y^4+70x^4z^4+70y^4z^4-56x^6yz-56xy^6z-56xyz^6+168x^5y^2z+168x^5yz^2+168x^2y^5z+168x^2yz^5+168xy^5z^2+168xy^2z^5+280x^4y^3z+280x^4yz^3+280x^3y^4z+280x^3yz^4+280xy^4z^3+280xy^3z^4+420x^4y^2z^2+420x^2y^4z^2+420x^2y^2z^4-560x^3y^3z^2-560x^3y^2z^3-560x^2y^3z^3)"
]

# CASOS LÍMITE - Productos de polinomios extremadamente complejos (REEMPLAZADO: antes eran racionales extremos)
EJEMPLOS_CASOS_LIMITE_POLINOMIOS_EXTREMOS = [
    "(x^7+7x^6+21x^5+35x^4+35x^3+21x^2+7x+1)(x^7-7x^6+21x^5-35x^4+35x^3-21x^2+7x-1)(x^5+1)(x^5-1)",
    "(x^9+9x^8+36x^7+84x^6+126x^5+126x^4+84x^3+36x^2+9x+1)(x^9-9x^8+36x^7-84x^6+126x^5-126x^4+84x^3-36x^2+9x-1)(x^7+1)(x^7-1)",
    "(x^{11}+11x^{10}+55x^9+165x^8+330x^7+462x^6+462x^5+330x^4+165x^3+55x^2+11x+1)(x^{11}-11x^{10}+55x^9-165x^8+330x^7-462x^6+462x^5-330x^4+165x^3-55x^2+11x-1)(x^9+1)(x^9-1)",
    "(x^{13}+13x^{12}+78x^{11}+286x^{10}+715x^9+1287x^8+1716x^7+1716x^6+1287x^5+715x^4+286x^3+78x^2+13x+1)(x^{13}-13x^{12}+78x^{11}-286x^{10}+715x^9-1287x^8+1716x^7-1716x^6+1287x^5-715x^4+286x^3-78x^2+13x-1)(x^{11}+1)(x^{11}-1)",
    "(x^{15}+15x^{14}+105x^{13}+455x^{12}+1365x^{11}+3003x^{10}+5005x^9+6435x^8+6435x^7+5005x^6+3003x^5+1365x^4+455x^3+105x^2+15x+1)(x^{15}-15x^{14}+105x^{13}-455x^{12}+1365x^{11}-3003x^{10}+5005x^9-6435x^8+6435x^7-5005x^6+3003x^5-1365x^4+455x^3-105x^2+15x-1)(x^{13}+1)(x^{13}-1)",
    "(x^{17}+17x^{16}+136x^{15}+680x^{14}+2380x^{13}+6188x^{12}+12376x^{11}+19448x^{10}+24310x^9+24310x^8+19448x^7+12376x^6+6188x^5+2380x^4+680x^3+136x^2+17x+1)(x^{17}-17x^{16}+136x^{15}-680x^{14}+2380x^{13}-6188x^{12}+12376x^{11}-19448x^{10}+24310x^9-24310x^8+19448x^7-12376x^6+6188x^5-2380x^4+680x^3-136x^2+17x-1)(x^{15}+1)(x^{15}-1)"
]

# Ejemplos con productos de polinomios usando delimitadores LaTeX (REEMPLAZADO: antes era Cheat Sheet)
EJEMPLOS_DELIMITADORES_LATEX = [
    r"\left(x+y\right)\left(x-y\right)",
    r"\left(a+b\right)\left(a-b\right)",
    r"\left(x^2+y^2\right)\left(x^2-y^2\right)",
    r"\left(\alpha+\beta\right)\left(\alpha-\beta\right)",
    r"\left(\lambda+1\right)\left(\lambda-1\right)",
    r"\left(\theta^2+\phi^2\right)\left(\theta^2-\phi^2\right)",
    r"\left[x+y\right]\left[x-y\right]",
    r"\left\{a+b\right\}\left\{a-b\right\}",
    r"\left|x+1\right|\left|x-1\right|",
    r"\left\langle x^2+1\right\rangle\left\langle x-1\right\rangle"
]

# CASOS EXTREMOS - Multiplicatorias extremas
EJEMPLOS_MULTIPLICATORIAS_EXTREMAS = [
    r"\prod_{i=1}^{n} (i+1)(i-1)",
    r"\prod_{k=1}^{m} (k^2+1)(k^2-1)",
    r"\prod_{j=1}^{p} (j^3+3j^2+3j+1)(j^3-3j^2+3j-1)",
    r"\prod_{i=1}^{q} (i^4+4i^3+6i^2+4i+1)(i^4-4i^3+6i^2-4i+1)",
    r"\prod_{n=1}^{r} (n^5+5n^4+10n^3+10n^2+5n+1)(n^5-5n^4+10n^3-10n^2+5n-1)",
    r"\prod_{m=1}^{s} (m^6+6m^5+15m^4+20m^3+15m^2+6m+1)(m^6-6m^5+15m^4-20m^3+15m^2-6m+1)"
]

# CASOS LÍMITE - Multiplicatorias en LaTeX
EJEMPLOS_CASOS_LIMITE_MULTIPLICATORIAS = [
    r"\displaystyle\prod_{i=1}^{n} \left(i+1\right)\left(i-1\right)",
    r"\displaystyle\prod\limits_{k=1}^{m} \left(k^2+1\right)\left(k^2-1\right)",
    r"\prod\nolimits_{j=1}^{p} \left(j^3+3j^2+3j+1\right)\left(j^3-3j^2+3j-1\right)",
    r"\prod_{i=1}^{q} \left(i^4+4i^3+6i^2+4i+1\right)\left(i^4-4i^3+6i^2-4i+1\right)",
    r"\displaystyle\prod_{n=1}^{r} \left(n^5+5n^4+10n^3+10n^2+5n+1\right)\left(n^5-5n^4+10n^3-10n^2+5n-1\right)",
    r"\prod\limits_{m=1}^{s} \left(m^6+6m^5+15m^4+20m^3+15m^2+6m+1\right)\left(m^6-6m^5+15m^4-20m^3+15m^2-6m+1\right)"
]

# CASOS EXTREMOS - Integrales extremas
EJEMPLOS_INTEGRALES_EXTREMAS = [
    r"\int_{-\infty}^{\infty} (x^7+7x^6+21x^5+35x^4+35x^3+21x^2+7x+1)(x^7-7x^6+21x^5-35x^4+35x^3-21x^2+7x-1) e^{-x^2} dx",
    r"\int_{0}^{\pi} (x^8+8x^7+28x^6+56x^5+70x^4+56x^3+28x^2+8x+1)(x^8-8x^7+28x^6-56x^5+70x^4-56x^3+28x^2-8x+1) \sin(x) dx",
    r"\int_{-1}^{1} (x^9+9x^8+36x^7+84x^6+126x^5+126x^4+84x^3+36x^2+9x+1)(x^9-9x^8+36x^7-84x^6+126x^5-126x^4+84x^3-36x^2+9x-1) \sqrt{1-x^2} dx",
    r"\int_{0}^{1} (x^{10}+10x^9+45x^8+120x^7+210x^6+252x^5+210x^4+120x^3+45x^2+10x+1)(x^{10}-10x^9+45x^8-120x^7+210x^6-252x^5+210x^4-120x^3+45x^2-10x+1) \ln(x) dx",
    r"\int_{0}^{\infty} (x^{11}+11x^{10}+55x^9+165x^8+330x^7+462x^6+462x^5+330x^4+165x^3+55x^2+11x+1)(x^{11}-11x^{10}+55x^9-165x^8+330x^7-462x^6+462x^5-330x^4+165x^3-55x^2+11x-1) e^{-x} dx",
    r"\int_{-\pi}^{\pi} (x^{12}+12x^{11}+66x^{10}+220x^9+495x^8+792x^7+924x^6+792x^5+495x^4+220x^3+66x^2+12x+1)(x^{12}-12x^{11}+66x^{10}-220x^9+495x^8-792x^7+924x^{6}-792x^{5}+495x^{4}-220x^{3}+66x^{2}-12x+1) \cos(x) dx"
]

# CASOS LÍMITE - Notaciones mixtas y raras
EJEMPLOS_CASOS_LIMITE_NOTACIONES_RARAS = [
    r"\frac{d}{dx}\left[\left(x^2+1\right)\left(x-1\right)\right]",
    r"\int_{0}^{1} \left(\left(x+1\right)\left(x-1\right)\right) dx",
    r"\prod_{i=1}^{n} \left(\left(i+1\right)\left(i-1\right)\right)",
    r"\sum_{k=1}^{m} \left[\left(k^2+1\right)\left(k^2-1\right)\right]",
    r"\frac{d^2}{dx^2}\left\{\left(x^3+3x^2+3x+1\right)\left(x^3-3x^2+3x-1\right)\right\}",
    r"\int_{-\pi}^{\pi} \left|\left(x+1\right)\left(x-1\right)\right| \sin(x) dx"
]

# Ejemplos con diferentes notaciones de multiplicación en LaTeX
EJEMPLOS_NOTACIONES_MULTIPLICACION = [
    r"(x+1)(x-1)",
    r"(x+1)\cdot(x-1)",
    r"(x+1)\times(x-1)",
    r"(x+1)\,(x-1)",
    r"(x+1)\;(x-1)",
    r"(x+1)\quad(x-1)",
    r"(x+y)\cdot(x-y)",
    r"(a+b)\times(a-b)",
    r"(x^2+1)\,(x-1)",
    r"(x^2+y^2)\;(x^2-y^2)"
]

# Ejemplos con notaciones mixtas de factores
EJEMPLOS_NOTACIONES_MIXTAS = [
    r"(x+1)\left[x-1\right]",
    r"\left(a+b\right)(a-b)",
    r"\left[x^2+y^2\right](x^2-y^2)",
    r"(\alpha+\beta)(\alpha-\beta)",
    r"\left\{\lambda+1\right\}\cdot(\lambda-1)",
    r"(p+q)(p-q)",
    r"(m+n)(m-n)"
]

# Ejemplos con comandos LaTeX de espaciado y alineación
EJEMPLOS_ESPACIADO_LATEX = [
    r"(x+1)(x-1)",
    r"(a+b)(a-b)",
    r"(x^2+y^2)(x^2-y^2)",
    r"(\alpha+\beta)(\alpha-\beta)",
    r"(\lambda+1)(\lambda-1)",
    r"(p+q)(p-q)",
    r"(m+n)(m-n)"
]

EJEMPLOS_DELIMITADORES_LATEX = [
    r"\left(x_1 + y_1\right)\left(x_1 - y_1\right)",
    r"\left(a_2 + b_2\right)\left(a_2 - b_2\right)",
    r"\left(x^2 + y^2\right)\left(x^2 - y^2\right)",
    r"\left(x+1\right)\left(x-1\right)",
    r"\left(a+b\right)\left(a-b\right)",
    r"\left(x+1\right)\left[x-1\right]",
    r"\left\{x+2\right\}\left(x-2\right)",
    r"\left(\alpha + \beta\right)\left(\alpha - \beta\right)",
    r"\left(\lambda^2 + 1\right)\left(\lambda - 1\right)",
    r"\left(2x+3\right)\left(x-4\right)",
    r"\left(5y^2+1\right)\left(y-2\right)",
    r"\sum_{k=1}^3 \left(k+1\right)\left(k-1\right)",
    r"\sum_{n=0}^2 \left(n^2+1\right)\left(n-1\right)",
    r"\int_0^1 \left(x+1\right)\left(x-1\right) dx",
    r"\int_{-1}^1 \left(x^2+2x+1\right)\left(x-1\right) dx",
    r"\left(x+1\right)^2\left(x-1\right)",
    r"\left(y-2\right)^3\left(y+2\right)",
    r"\left(x+y+z\right)\left(x-y-z\right)",
    r"\left(a+b+c\right)\left(a-b+c\right)",
    r"\left(x+1\right)\left(x-1\right)",
    r"\left[x^2+1\right]\left[x-1\right]"
]

# Ejemplos con productos de polinomios usando variables griegas (REEMPLAZADO: antes era Letras y Números Griegos)
EJEMPLOS_VARIABLES_GRIEGAS = [
    r"(\alpha + \beta)(\alpha - \beta)",
    r"(\lambda^2 + 1)(\lambda - 1)",
    r"(\alpha_1 + \beta_2)(\alpha_1 - \beta_2)",
    r"(\lambda_3^2 + 1)(\lambda_3 - 1)",
    r"(\theta^2 + \phi^2)(\theta^2 - \phi^2)",
    r"(\gamma + \delta)(\gamma - \delta)",
    r"(\epsilon^2 + \zeta^2)(\epsilon - \zeta)",
    r"(\eta + \kappa)(\eta^2 - \kappa^2)",
    r"(\mu^3 + 3\mu^2\nu + 3\mu\nu^2 + \nu^3)(\mu - \nu)",
    r"(\omega^2 + \pi)(\omega - \sqrt{\pi})"
]

# === NUEVA CATEGORÍA: Ejemplos Cheat Sheet (LaTeX) ===
EJEMPLOS_CHEATSHEET = [
    r"(x_{1}^{2}+2x_{1}+1)(x_{1}-1)",
    r"(y_{2}^{2}+y_{2}+1)(y_{2}-1)",
    r"(a^{2}+2a+1)(a-1)",
    r"(\alpha^{2}+2\alpha+1)(\alpha-1)",
    r"(\lambda^{2}+1)(\lambda-1)",
    r"(x^{2}+y^{2})(x^{2}-y^{2})",
    r"(x^{2}+\alpha^{2})(x^{2}-\alpha^{2})",
    r"(x^{2}+2x+1)(x^{2}-2x+1)",
    r"(x^{3}+1)(x^{3}-1)",
    r"(x^{4}+1)(x^{4}-1)",
    r"(x^{2}+xy+y^{2})(x^{2}-xy+y^{2})",
    r"(\frac{1}{2}x+1)(x-2)",
    r"(\frac{3}{4}x-2)(x+4)",
    r"(x_{i}+y_{j})(x_{i}-y_{j})",
    r"(\theta^{2}+\phi^{2})(\theta^{2}-\phi^{2})",
    r"(x_{a}^{2}+2x_{a}+1)(x_{a}-1)",
    r"(\beta^{2}+2\beta+1)(\beta-1)",
    r"(x^{2}+2x+1)(x-1)",
    r"(x^{2}+1)(x-1)"
]

# Diccionario con todas las categorías NO-EXTREMAS (solo ejemplos <1200)
CATEGORIAS_EJEMPLOS = {
    "Básicos": EJEMPLOS_BASICOS,
    "Productos Binomios": EJEMPLOS_PRODUCTOS_BINOMIOS,
    "Productos Potencias": EJEMPLOS_PRODUCTOS_POTENCIAS,
    "Sumatorias": EJEMPLOS_SUMATORIAS,
    "Integrales": EJEMPLOS_INTEGRALES,
    "Multiplicatorias": MULTIPLICATORIAS,
    "Derivadas": EJEMPLOS_DERIVADAS,
    "Polinomios Complejos": EJEMPLOS_POLINOMIOS_COMPLEJOS,
    "Productos Cuadráticos": EJEMPLOS_PRODUCTOS_CUADRATICOS,
    "Productos Cúbicos": EJEMPLOS_PRODUCTOS_CUBICOS,
    "Binomios a Potencias": EJEMPLOS_BINOMIOS_POTENCIAS,
    "Trinomios": EJEMPLOS_TRINOMIOS,
    "Polinomios Superiores": EJEMPLOS_POLINOMIOS_SUPERIORES,
    "Múltiples Variables": EJEMPLOS_MULTIPLES_VARIABLES,
    "Con Coeficientes": EJEMPLOS_COEFICIENTES,
    "Polinomios Grado Alto": EJEMPLOS_POLINOMIOS_GRADO_ALTO,
    "Funciones Trigonométricas": EJEMPLOS_TRIGONOMETRICOS,
    "Integrales Trigonométricas": EJEMPLOS_INTEGRALES_TRIGONOMETRICAS,
    "Derivadas Trigonométricas": EJEMPLOS_DERIVADAS_TRIGONOMETRICAS,
    "Sumatorias Trigonométricas": EJEMPLOS_SUMATORIAS_TRIGONOMETRICAS,
    "Productos Trigonométricos": EJEMPLOS_PRODUCTOS_TRIGONOMETRICOS,
    "Casos Límite - Polinomios": EJEMPLOS_CASOS_LIMITE_POLINOMIOS,
    "Casos Límite - Polinomios Altos": EJEMPLOS_CASOS_LIMITE_POLINOMIOS_ALTOS,
    "Casos Límite - Sumatorias": EJEMPLOS_CASOS_LIMITE_SUMATORIAS,
    "Casos Límite - Integrales": EJEMPLOS_CASOS_LIMITE_INTEGRALES,
    "Casos Límite - Derivadas": EJEMPLOS_CASOS_LIMITE_DERIVADAS,
    "Casos Límite - Multivariables": EJEMPLOS_CASOS_LIMITE_MULTIVARIABLES,
    "Casos Límite - Polinomios Extremos": EJEMPLOS_CASOS_LIMITE_POLINOMIOS_EXTREMOS,
    "Delimitadores LaTeX": EJEMPLOS_DELIMITADORES_LATEX,
    "Variables Griegas": EJEMPLOS_VARIABLES_GRIEGAS,
    "Coeficientes Fraccionarios y Negativos": EJEMPLOS_COEFICIENTES_FRACCIONARIOS,
    "Subíndices y Superíndices": EJEMPLOS_SUBINDICES_SUPERINDICES,
    "Mayúsculas y Minúsculas": EJEMPLOS_MAYUSCULAS_MINUSCULAS,
    "Variables Distintas": EJEMPLOS_VARIABLES_DISTINTAS,
    "Ejemplos Cheat Sheet (LaTeX)": EJEMPLOS_CHEATSHEET_LATEX,
    "Multiplicatorias Extremas": EJEMPLOS_MULTIPLICATORIAS_EXTREMAS,
    "Casos Límite - Multiplicatorias": EJEMPLOS_CASOS_LIMITE_MULTIPLICATORIAS,
    "Casos Límite - Notaciones Raras": EJEMPLOS_CASOS_LIMITE_NOTACIONES_RARAS,
    "Notaciones de Multiplicación": EJEMPLOS_NOTACIONES_MULTIPLICACION,
    "Notaciones Mixtas": EJEMPLOS_NOTACIONES_MIXTAS,
    "Espaciado LaTeX": EJEMPLOS_ESPACIADO_LATEX
}

# === EJEMPLOS ESPECIALES (>1200 caracteres, cumplen premisa pero NO procesables) ===
EJEMPLOS_MAS_1200 = [
    r"\frac{d^{15}}{dx^{15}}[(x^{20}+20x^{19}+190x^{18}+1140x^{17}+4845x^{16}+15504x^{15}+38760x^{14}+77520x^{13}+125970x^{12}+167960x^{11}+184756x^{10}+167960x^9+125970x^8+77520x^7+38760x^6+15504x^5+4845x^4+1140x^3+190x^2+20x+1)(x^{20}-20x^{19}+190x^{18}-1140x^{17}+4845x^{16}-15504x^{15}+38760x^{14}-77520x^{13}+125970x^{12}-167960x^{11}+184756x^{10}-167960x^9+125970x^8-77520x^7+38760x^6-15504x^5+4845x^4-1140x^3+190x^2-20x+1)]",
    r"\sum_{n=1}^{50} \frac{(n^{12}+12n^{11}+66n^{10}+220n^9+495n^8+792n^7+924n^6+792n^5+495n^4+220n^3+66n^2+12n+1)(n^{12}-12n^{11}+66n^{10}-220n^9+495n^8-792n^7+924n^6-792n^5+495n^4-220n^3+66n^2-12n+1)}{(n^6+1)(n^6-1)} \cdot \frac{(n^8+8n^7+28n^6+56n^5+70n^4+56n^3+28n^2+8n+1)(n^8-8n^7+28n^6-56n^5+70n^4-56n^3+28n^2-8n+1)}{(n^4+1)(n^4-1)}",
    r"\int_{-\infty}^{\infty} \frac{(x^{16}+16x^{15}+120x^{14}+560x^{13}+1820x^{12}+4368x^{11}+8008x^{10}+11440x^9+12870x^8+11440x^7+8008x^6+4368x^5+1820x^4+560x^3+120x^2+16x+1)(x^{16}-16x^{15}+120x^{14}-560x^{13}+1820x^{12}-4368x^{11}+8008x^{10}-11440x^9+12870x^8-11440x^7+8008x^6-4368x^5+1820x^4-560x^3+120x^2-16x+1)}{(x^2+1)(x^2-1)} e^{-x^2} dx \cdot \int_{0}^{1} \frac{(x^{14}+14x^{13}+91x^{12}+364x^{11}+1001x^{10}+2002x^9+3003x^8+3432x^7+3003x^6+2002x^5+1001x^4+364x^3+91x^2+14x+1)(x^{14}-14x^{13}+91x^{12}-364x^{11}+1001x^{10}-2002x^9+3003x^8-3432x^7+3003x^6-2002x^5+1001x^4-364x^3+91x^2-14x+1)}{(x^6+1)(x^6-1)} dx"
]

CATEGORIA_MAS_1200 = {">1200": EJEMPLOS_MAS_1200}

# Ejemplos EXTREMOS (>=1200 caracteres) - NO PROCESABLES por el parser
# Estos ejemplos superan el límite de 1200 caracteres y causan errores internos de latex2sympy2

EJEMPLOS_EXTREMOS_FRACCIONES = [
    r"\frac{(x^{25}+25x^{24}+300x^{23}+2300x^{22}+12650x^{21}+53130x^{20}+177100x^{19}+480700x^{18}+1081575x^{17}+2042975x^{16}+3268760x^{15}+4457400x^{14}+5200300x^{13}+5200300x^{12}+4457400x^{11}+3268760x^{10}+2042975x^9+1081575x^8+480700x^7+177100x^6+53130x^5+12650x^4+2300x^3+300x^2+25x+1)(x^{25}-25x^{24}+300x^{23}-2300x^{22}+12650x^{21}-53130x^{20}+177100x^{19}-480700x^{18}+1081575x^{17}-2042975x^{16}+3268760x^{15}-4457400x^{14}+5200300x^{13}-5200300x^{12}+4457400x^{11}-3268760x^{10}+2042975x^9-1081575x^8+480700x^7-177100x^6+53130x^5-12650x^4+2300x^3-300x^2+25x-1)}{(x^{15}+1)(x^{15}-1)}",
    r"\frac{(x^{30}+30x^{29}+435x^{28}+4060x^{27}+27405x^{26}+142506x^{25}+593775x^{24}+2035800x^{23}+5852925x^{22}+14307150x^{21}+30045015x^{20}+54627300x^{19}+86493225x^{18}+119759850x^{17}+145422675x^{16}+155117520x^{15}+145422675x^{14}+119759850x^{13}+86493225x^{12}+54627300x^{11}+30045015x^{10}+14307150x^9+5852925x^8+2035800x^7+593775x^6+142506x^5+27405x^4+4060x^3+435x^2+30x+1)(x^{30}-30x^{29}+435x^{28}-4060x^{27}+27405x^{26}-142506x^{25}+593775x^{24}-2035800x^{23}+5852925x^{22}-14307150x^{21}+30045015x^{20}-54627300x^{19}+86493225x^{18}-119759850x^{17}+145422675x^{16}-155117520x^{15}+145422675x^{14}-119759850x^{13}+86493225x^{12}-54627300x^{11}+30045015x^{10}-14307150x^9+5852925x^8-2035800x^7+593775x^6-142506x^5+27405x^4-4060x^3+435x^2-30x+1)}{(x^{20}+1)(x^{20}-1)}"
]

EJEMPLOS_EXTREMOS_DERIVADAS = [
    r"\frac{d^{10}}{dx^{10}}[(x^{12}+12x^{11}+66x^{10}+220x^9+495x^8+792x^7+924x^6+792x^5+495x^4+220x^3+66x^2+12x+1)(x^{12}-12x^{11}+66x^{10}-220x^9+495x^8-792x^7+924x^6-792x^5+495x^4-220x^3+66x^2-12x+1)]",
    r"\frac{\partial^{10}}{\partial x^5 \partial y^5}[(x^{12}+12x^{11}+66x^{10}+220x^9+495x^8+792x^7+924x^6+792x^5+495x^4+220x^3+66x^2+12x+1)(y^{12}+12y^{11}+66y^{10}+220y^9+495y^8+792y^7+924y^6+792y^5+495y^4+220y^3+66y^2+12y+1)]"
]

EJEMPLOS_EXTREMOS_INTEGRALES = [
    r"\left(\int_0^1 (x^8+8x^7+28x^6+56x^5+70x^4+56x^3+28x^2+8x+1)(x^8-8x^7+28x^6-56x^5+70x^4-56x^3+28x^2-8x+1) dx\right) \cdot \left(\int_0^1 (x^9+9x^8+36x^7+84x^6+126x^5+126x^4+84x^3+36x^2+9x+1)(x^9-9x^8+36x^7-84x^6+126x^5-126x^4+84x^3-36x^2+9x-1) dx\right)",
    r"\int_{-\infty}^{\infty} \frac{(x^{18}+18x^{17}+153x^{16}+816x^{15}+3060x^{14}+8568x^{13}+18564x^{12}+31824x^{11}+43758x^{10}+48620x^9+43758x^8+31824x^7+18564x^6+8568x^5+3060x^4+816x^3+153x^2+18x+1)(x^{18}-18x^{17}+153x^{16}-816x^{15}+3060x^{14}-8568x^{13}+18564x^{12}-31824x^{11}+43758x^{10}-48620x^9+43758x^8-31824x^7+18564x^6-8568x^5+3060x^4-816x^3+153x^2-18x+1)}{(x^2+1)(x^2-1)} dx"
]

EJEMPLOS_EXTREMOS_SUMATORIAS = [
    r"\sum_{n=1}^{100} \frac{(n^{15}+15n^{14}+105n^{13}+455n^{12}+1365n^{11}+3003n^{10}+5005n^9+6435n^8+6435n^7+5005n^6+3003n^5+1365n^4+455n^3+105n^2+15n+1)(n^{15}-15n^{14}+105n^{13}-455n^{12}+1365n^{11}-3003n^{10}+5005n^9-6435n^8+6435n^7-5005n^6+3003n^5-1365n^4+455n^3-105n^2+15n-1)}{(n^7+1)(n^7-1)}",
    r"\sum_{i=1}^{10} \sum_{j=1}^{10} \sum_{k=1}^{10} \frac{(i^5+j^5+k^5+5i^4j+5i^4k+5ij^4+5ik^4+5j^4k+5jk^4+10i^3j^2+10i^3k^2+10i^2j^3+10i^2k^3+10j^3k^2+10j^2k^3+20i^3jk+20ij^3k+20ijk^3+30i^2j^2k+30i^2jk^2+30ij^2k^2)(i^5+j^5+k^5-5i^4j-5i^4k-5ij^4-5ik^4-5j^4k-5jk^4+10i^3j^2+10i^3k^2+10i^2j^3+10i^2k^3+10j^3k^2+10j^2k^3-20i^3jk-20ij^3k-20ijk^3+30i^2j^2k+30i^2jk^2+30ij^2k^2)}{(i^3+j^3+k^3)(i^3-j^3-k^3)}"
]

EJEMPLOS_EXTREMOS_POLINOMIOS = [
    "(x^{50}+50x^{49}+1225x^{48}+19600x^{47}+230300x^{46}+2118760x^{45}+15815800x^{44}+99884400x^{43}+536878650x^{42}+2505433700x^{41}+10272278170x^{40}+37353738800x^{39}+121399651100x^{38}+354860518600x^{37}+937845656300x^{36}+2250829575120x^{35}+4923689695575x^{34}+9847379391150x^{33}+18053528883775x^{32}+30405943383200x^{31}+47129212243960x^{30}+67327446062800x^{29}+88749815264600x^{28}+108043253365600x^{27}+121548660036300x^{26}+126410606437752x^{25}+121548660036300x^{24}+108043253365600x^{23}+88749815264600x^{22}+67327446062800x^{21}+47129212243960x^{20}+30405943383200x^{19}+18053528883775x^{18}+9847379391150x^{17}+4923689695575x^{16}+2250829575120x^{15}+937845656300x^{14}+354860518600x^{13}+121399651100x^{12}+37353738800x^{11}+10272278170x^{10}+2505433700x^9+536878650x^8+99884400x^7+15815800x^6+2118760x^5+230300x^4+19600x^3+1225x^2+50x+1)(x^{50}-50x^{49}+1225x^{48}-19600x^{47}+230300x^{46}-2118760x^{45}+15815800x^{44}-99884400x^{43}+536878650x^{42}-2505433700x^{41}+10272278170x^{40}-37353738800x^{39}+121399651100x^{38}-354860518600x^{37}+937845656300x^{36}-2250829575120x^{35}+4923689695575x^{34}-9847379391150x^{33}+18053528883775x^{32}-30405943383200x^{31}+47129212243960x^{30}-67327446062800x^{29}+88749815264600x^{28}-108043253365600x^{27}+121548660036300x^{26}-126410606437752x^{25}+121548660036300x^{24}-108043253365600x^{23}+88749815264600x^{22}-67327446062800x^{21}+47129212243960x^{20}-30405943383200x^{19}+18053528883775x^{18}-9847379391150x^{17}+4923689695575x^{16}-2250829575120x^{15}+937845656300x^{14}-354860518600x^{13}+121399651100x^{12}-37353738800x^{11}+10272278170x^{10}-2505433700x^9+536878650x^8-99884400x^7+15815800x^6-2118760x^5+230300x^4-19600x^3+1225x^2-50x+1)"
]


EJEMPLOS_EXTREMOS_MULTIVARIABLES = [
    "(x^{10}+y^{10}+z^{10}+10x^9y+10x^9z+10xy^9+10xz^9+10y^9z+10yz^9+45x^8y^2+45x^8z^2+45x^2y^8+45x^2z^8+45y^8z^2+45y^2z^8+120x^7y^3+120x^7z^3+120x^3y^7+120x^3z^7+120y^7z^3+120y^3z^7+210x^6y^4+210x^6z^4+210x^4y^6+210x^4z^6+210y^6z^4+210y^4z^6+252x^5y^5+252x^5z^5+252y^5z^5+420x^7y^2z+420x^7yz^2+420x^2y^7z+420x^2yz^7+420x^2y^7z+420xy^2z^7+1260x^6y^3z+1260x^6yz^3+1260x^3y^6z+1260x^3yz^6+1260x^3y^6z+1260xy^3z^6+2520x^5y^4z+2520x^5yz^4+2520x^4y^5z+2520x^4yz^5+2520x^4y^5z+2520xy^4z^5+3150x^5y^3z^2+3150x^5y^2z^3+3150x^3y^5z^2+3150x^3y^2z^5+3150x^2y^5z^3+3150x^2y^3z^5+4200x^4y^4z^2+4200x^4y^2z^4+4200x^2y^4z^4+6300x^4y^3z^3+6300x^3y^4z^3+6300x^3y^3z^4)(x^{10}+y^{10}+z^{10}-10x^9y-10x^9z-10xy^9-10xz^9-10y^9z-10yz^9+45x^8y^2+45x^8z^2+45x^2y^8+45x^2z^8+45y^8z^2+45y^2z^8+120x^7y^3+120x^7z^3+120x^3y^7+120x^3z^7+120y^7z^3+120y^3z^7+210x^6y^4+210x^6z^4+210x^4y^6+210x^4z^6+210y^6z^4+210y^4z^6+252x^5y^5+252x^5z^5+252y^5z^5-420x^7y^2z-420x^7yz^2-420x^2y^7z-420x^2yz^7-420x^2y^7z-420xy^2z^7+1260x^6y^3z+1260x^6yz^3+1260x^3y^6z+1260x^3yz^6+1260x^3y^6z+1260xy^3z^6+2520x^5y^4z+2520x^5yz^4+2520x^4y^5z+2520x^4yz^5+2520x^4y^5z+2520xy^4z^5+3150x^5y^3z^2+3150x^5y^2z^3+3150x^3y^5z^2+3150x^3y^2z^5+3150x^2y^5z^3+3150x^2y^3z^5+4200x^4y^4z^2+4200x^4y^2z^4+4200x^2y^4z^4-6300x^4y^3z^3-6300x^3y^4z^3-6300x^3y^3z^4)"
]

# Diccionario con todas las categorías EXTREMAS (solo ejemplos >=1200)
CATEGORIAS_EJEMPLOS_EXTREMOS = {
    "Fracciones Extremas": EJEMPLOS_EXTREMOS_FRACCIONES,
    "Derivadas Extremas": EJEMPLOS_EXTREMOS_DERIVADAS,
    "Integrales Extremas": EJEMPLOS_EXTREMOS_INTEGRALES,
    "Sumatorias Extremas": EJEMPLOS_EXTREMOS_SUMATORIAS,
    "Polinomios Extremos": EJEMPLOS_EXTREMOS_POLINOMIOS,
    "Multivariables Extremas": EJEMPLOS_EXTREMOS_MULTIVARIABLES,
    "Integrales Extremas (Especiales)": EJEMPLOS_INTEGRALES_EXTREMAS,
    "Multiplicatorias Extremas": EJEMPLOS_MULTIPLICATORIAS_EXTREMAS,
    "Casos Límite - Multiplicatorias": EJEMPLOS_CASOS_LIMITE_MULTIPLICATORIAS,
    "Casos Límite - Notaciones Raras": EJEMPLOS_CASOS_LIMITE_NOTACIONES_RARAS
}

# Configuraciones para la GUI
GUI_CONFIG = {
    "titulo": "ExpaAlgebraico - Sistema de Expansión Algebraica",
    "subtitulo": "Sistema Robusto para Expansión de Expresiones Matemáticas en LaTeX",
    "ancho_ventana": 1200,
    "alto_ventana": 800,
    "color_fondo": "#f0f0f0",
    "color_principal": "#2c3e50",
    "color_secundario": "#3498db",
    "color_exito": "#27ae60",
    "color_error": "#e74c3c",
    "color_advertencia": "#f39c12"
}

# Mensajes de error comunes
ERROR_MESSAGES = {
    'no_expression': "Por favor, ingresa una expresión.",
    'invalid_expression': "La expresión ingresada no es válida.",
    'no_image': "Por favor, carga una imagen primero.",
    'ocr_failed': "No se pudo extraer texto de la imagen.",
    'processing_error': "Error al procesar la expresión.",
    'file_save_error': "Error al guardar el archivo.",
    'file_load_error': "Error al cargar el archivo.",
    'no_results': "No hay resultados para mostrar."
}

# Configuración de archivos

# === NUEVA CATEGORÍA: Ejemplos Cheat Sheet (LaTeX) ===

FILE_CONFIG = {
    'supported_image_types': [
        ("Archivos de imagen", "*.png *.jpg *.jpeg *.gif *.bmp *.tiff"),
        ("PNG", "*.png"),
        ("JPEG", "*.jpg *.jpeg"),
        ("Todos los archivos", "*.*")
    ],
    'supported_save_types': [
        ("Archivo de texto", "*.txt"),
        ("Archivo LaTeX", "*.tex"),
        ("Todos los archivos", "*.*")
    ],
    'default_extension': '.txt'
}
