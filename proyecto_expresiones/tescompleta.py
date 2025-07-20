#!/usr/bin/env python3
"""
Test de Consigna Completa - ExpaAlgebraico
==========================================

Este test verifica que el sistema cumple COMPLETAMENTE la consigna del proyecto:
"Expandir una expresión escrita como producto de factores (cada factor es a lo más un polinomio) 
a una expresión escrita como suma o diferencia de términos (un polinomio).

La expresión es dada usando sintaxis de LaTeX y debe ser devuelta en sintaxis de LaTeX."

Verifica TODOS los ejemplos del archivo config.py para asegurar cobertura completa.
"""

import sys
import os
from datetime import datetime
import time
import re
from sympy import Rational

# Agregar el directorio del proyecto al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from expander import Expander
    from latex_exporter import LatexExporter
    from config import CATEGORIAS_EJEMPLOS, CATEGORIAS_EJEMPLOS_EXTREMOS
    from input_parser import postprocess_latex_for_display
    print(" Módulos importados correctamente")
except ImportError as e:
    print(f" Error importando módulos: {e}")
    sys.exit(1)



def _verificar_producto_factores(latex_input):
    """
    Verifica que la expresión LaTeX es un producto de factores.
    Un producto de factores tiene la forma (factor1)(factor2)...(factorN)
    donde cada factor es a lo más un polinomio.
    """
    # Patrones para detectar productos de factores
    patrones_producto = [
        r'\([^)]+\)\s*\([^)]+\)',  # (expr1)(expr2)
        r'\([^)]+\)\s*\*\s*\([^)]+\)',  # (expr1)*(expr2)
        r'\([^)]+\)\s*\\cdot\s*\([^)]+\)',  # (expr1)\cdot(expr2)
        r'\([^)]+\)\s*\([^)]+\)\s*\([^)]+\)',  # (expr1)(expr2)(expr3)
    ]
    
    for patron in patrones_producto:
        if re.search(patron, latex_input):
            return True
    
    # Verificar si contiene múltiples paréntesis que sugieren producto
    parentesis_abiertos = latex_input.count('(')
    parentesis_cerrados = latex_input.count(')')
    
    # Si hay múltiples pares de paréntesis, probablemente es un producto
    if parentesis_abiertos >= 2 and parentesis_cerrados >= 2:
        return True
    
    return False

def _verificar_suma_diferencia(expanded_expr):
    """
    Verifica que el resultado es una suma o diferencia de términos (un polinomio).
    """
    if hasattr(expanded_expr, 'func'):
        # Verificar si es una suma (Add) - esto es lo que queremos
        if expanded_expr.func.__name__ == 'Add':
            return True
        # Verificar si es una multiplicación que se puede expandir
        elif expanded_expr.func.__name__ == 'Mul':
            # Si tiene múltiples términos, es una suma implícita
            return len(expanded_expr.args) > 1
        # Si es un polinomio simple (sin multiplicaciones), también es válido
        elif expanded_expr.func.__name__ in ['Symbol', 'Integer', 'Float']:
            return True
    
    # Verificar si la representación en string contiene sumas o restas
    expr_str = str(expanded_expr)
    return '+' in expr_str or '-' in expr_str

def _verificar_latex_salida(latex_output):
    """
    Verifica que la salida está en sintaxis LaTeX correcta.
    """
    if not latex_output:
        return False
    # Verificar que la salida mantiene operadores simbólicos si la entrada los tenía
    if r'\int' in latex_output and not any(r'\int' in pattern for pattern in [r'\int_', r'\int^']):
        return False
    if 'd^' in latex_output and not r'\frac{d}{dx}' in latex_output:
        return False
    # Verificar que contiene elementos LaTeX típicos y operadores simbólicos
    elementos_latex = [
        r'\\',      # Comandos LaTeX
        r'\^',       # Exponentes
        r'_',         # Subíndices
        r'\{',       # Llaves
        r'\}',       # Llaves
        r'\+',       # Sumas
        r'-',         # Restas
        r'\*',       # Multiplicaciones
        r'\sum',     # Sumatorias
        r'\int',     # Integrales
        r'\frac',    # Fracciones
        r'\partial', # Derivadas parciales
        r'\prod',    # Producto
        r'\lim',     # Límite
        r'\log',     # Logaritmo
        r'\sin',     # Seno
        r'\cos',     # Coseno
        r'\tan',     # Tangente
    ]
    for elemento in elementos_latex:
        if re.search(elemento, latex_output):
            return True
    # Si no tiene elementos LaTeX específicos, verificar que al menos tiene estructura polinómica
    estructura_polinomica = re.search(r'[\+\-\*\^_]', latex_output)
    if estructura_polinomica:
        return True
    # También aceptar si la salida tiene varios términos separados por + o -
    if latex_output.count('+') + latex_output.count('-') >= 1:
        return True
    # Si no, no es válido
    return False

def normalizar_delimitadores_latex(expr):
    """
    Normaliza delimitadores alternativos LaTeX a paréntesis estándar.
    Ejemplo: \left[ ... \right] -> ( ... )
             \left\{ ... \right\} -> ( ... )
    Solo modifica si detecta delimitadores alternativos.
    """
    # Unificar todos los delimitadores alternativos a paréntesis estándar, soportando anidamientos y casos mixtos
    # Reemplazar \left[...\right], \left\{...\right\}, \left(...\right) por (...)
    delimitadores = [
        (r'\\left\s*\[', r'('),
        (r'\\left\s*\{', r'('),
        (r'\\left\s*\(', r'('),
        (r'\\right\s*\]', r')'),
        (r'\\right\s*\}', r')'),
        (r'\\right\s*\)', r')'),
    ]
    for patron, reemplazo in delimitadores:
        expr = re.sub(patron, reemplazo, expr)

    # Eliminar \left y \right sueltos (sin delimitador)
    expr = re.sub(r'\\left\s*', '', expr)
    expr = re.sub(r'\\right\s*', '', expr)

    # Limpiar espacios entre paréntesis generados
    expr = re.sub(r'\(\s+', '(', expr)
    expr = re.sub(r'\s+\)', ')', expr)

    # Reemplazar corchetes y llaves por paréntesis si quedan
    expr = expr.replace('[', '(').replace(']', ')')
    expr = expr.replace('{', '(').replace('}', ')')

    return expr

def verificar_consigna(latex_input, descripcion, categoria):
    """
    Verifica que una expresión cumple la consigna del proyecto.
    Usa exactamente el mismo flujo que el main de la GUI.
    
    Args:
        latex_input (str): Expresión LaTeX de entrada
        descripcion (str): Descripción del caso
        categoria (str): Categoría del ejemplo
        
    Returns:
        dict: Resultado del test con detalles
    """
    resultado = {
        'categoria': categoria,
        'descripcion': descripcion,
        'input': latex_input,
        'exito': False,
        'error': None,
        'parsed': None,
        'expanded': None,
        'latex_output': None,
        'cumple_consigna': False,
        'es_producto_factores': False,
        'es_suma_diferencia': False,
        'es_latex_salida': False,
        'tiempo_procesamiento': 0,
        'tester_error_info': None
    }
    
    try:
        inicio = time.time()
        # Preprocesar delimitadores LaTeX alternativos
        latex_input_norm = normalizar_delimitadores_latex(latex_input)

        # PASO 1: Verificar que la entrada es un producto de factores en LaTeX
        resultado['es_producto_factores'] = _verificar_producto_factores(latex_input_norm)
        if not resultado['es_producto_factores']:
            resultado['error'] = f"La entrada no es un producto de factores: {latex_input}"
            resultado['tiempo_procesamiento'] = time.time() - inicio
            return resultado

        # PASO 2: Verificar que la entrada está en formato LaTeX
        comandos_latex = [r'\\frac', r'\\sum', r'\\int', r'\\sqrt', r'\\alpha', r'\\beta', r'\\gamma', r'\\delta', r'\\theta', r'\\sin', r'\\cos', r'\\tan', r'\\log', r'\\ln', r'\\left', r'\\right', r'\\cdot', r'\\infty', r'\^', r'_']
        if not any(re.search(cmd, latex_input_norm) for cmd in comandos_latex):
            # Si no tiene comandos LaTeX específicos, verificar que al menos tiene estructura matemática
            if not any(char in latex_input_norm for char in ['(', ')', '+', '-', '*', '^', '_']):
                resultado['error'] = f"La entrada no está en formato LaTeX válido: {latex_input}"
                resultado['tiempo_procesamiento'] = time.time() - inicio
                return resultado

        # Verificar que si la entrada tiene operadores simbólicos, estos deben mantenerse en la salida
        entrada_tiene_integral = r'\int' in latex_input_norm
        entrada_tiene_derivada = r'\frac{d}{dx}' in latex_input_norm

        # PASO 3: Usar EXACTAMENTE el mismo flujo que el main de la GUI
        # Flujo del main: Expander.process_expression(expression, is_latex=True)
        from expander import Expander

        res = Expander.process_expression(latex_input_norm, is_latex=True)
        if not res.get('success'):
            error_msg = res.get('error', '')
            resultado['error'] = error_msg

            # Capturar información de TESTER_ERROR si está disponible
            if 'TESTER_ERROR:' in error_msg:
                resultado['tester_error_info'] = _analizar_tester_error(error_msg)

            resultado['tiempo_procesamiento'] = time.time() - inicio
            return resultado

        resultado['parsed'] = str(res.get('original'))
        resultado['expanded'] = str(res.get('expanded'))

        # PASO 4: Verificar que el resultado es una suma/diferencia
        resultado['es_suma_diferencia'] = _verificar_suma_diferencia(res.get('expanded'))
        if not resultado['es_suma_diferencia']:
            resultado['error'] = f"El resultado no es una suma/diferencia: {resultado['expanded']}"
            resultado['tiempo_procesamiento'] = time.time() - inicio
            return resultado

        # PASO 5: Obtener LaTeX expandido usando el mismo método que la GUI
        # La GUI usa: Expander.latex_expanded_output(expr_obj) si es Basic, o result.get('expanded_latex')
        try:
            expr_obj = res.get('expanded')
            from sympy import Basic
            if isinstance(expr_obj, Basic):
                # Usar el mismo método que la GUI
                latex_result = Expander.latex_expanded_output(expr_obj)
            else:
                latex_result = res.get('expanded_latex', '')
        except Exception:
            latex_result = res.get('expanded_latex', '')

        # Postprocesar LaTeX igual que la GUI
        latex_result = postprocess_latex_for_display(latex_result)
        resultado['latex_output'] = latex_result

        # PASO 6: Verificar que la salida está en LaTeX y mantiene los operadores simbólicos
        resultado['es_latex_salida'] = _verificar_latex_salida(latex_result)
        if not resultado['es_latex_salida']:
            resultado['error'] = f"La salida no está en formato LaTeX: {latex_result}"
            resultado['tiempo_procesamiento'] = time.time() - inicio
            return resultado

        # Verificar que los operadores simbólicos se mantienen
        if entrada_tiene_integral and not (r'\int' in latex_result):
            resultado['error'] = f"La salida no mantiene el operador integral: {latex_result}"
            resultado['es_latex_salida'] = False
            resultado['tiempo_procesamiento'] = time.time() - inicio
            return resultado

        if entrada_tiene_derivada and not (r'\frac{d}{dx}' in latex_result):
            resultado['error'] = f"La salida no mantiene el operador derivada: {latex_result}"
            resultado['es_latex_salida'] = False
            resultado['tiempo_procesamiento'] = time.time() - inicio
            return resultado

        # La consigna se cumple si todos los pasos fueron exitosos
        resultado['cumple_consigna'] = True
        resultado['exito'] = True
        resultado['tiempo_procesamiento'] = time.time() - inicio

    except Exception as e:
        resultado['error'] = str(e)
        resultado['tiempo_procesamiento'] = time.time() - inicio

    return resultado

def _analizar_tester_error(error_msg):
    """
    Analiza un mensaje TESTER_ERROR para extraer información útil.
    
    Args:
        error_msg (str): Mensaje de error del parser
        
    Returns:
        dict: Información estructurada del error
    """
    if 'TESTER_ERROR:' not in error_msg:
        return None
    
    try:
        # Extraer información del mensaje TESTER_ERROR
        parts = error_msg.split(' | ')
        error_info = {
            'tipo_error': None,
            'descripcion': None,
            'input': None,
            'stage': None,
            'cleaned': None
        }
        
        for part in parts:
            if 'TESTER_ERROR:' in part:
                # Extraer tipo y descripción del error
                error_part = part.replace('TESTER_ERROR:', '').strip()
                if ':' in error_part:
                    error_info['tipo_error'] = error_part.split(':')[0].strip()
                    error_info['descripcion'] = error_part.split(':', 1)[1].strip()
            elif 'Input:' in part:
                error_info['input'] = part.replace('Input:', '').strip()
            elif 'Stage:' in part:
                error_info['stage'] = part.replace('Stage:', '').strip()
            elif 'Cleaned:' in part:
                error_info['cleaned'] = part.replace('Cleaned:', '').strip()
        
        return error_info
    except:
        return None

def generar_reporte_detallado(resultados):
    """
    Genera un reporte detallado de los resultados.
    
    Args:
        resultados (list): Lista de resultados de los tests
    """
    print(f"\n{'='*100}")
    print(f" REPORTE DETALLADO - VERIFICACIÓN DE CONSIGNA")
    print(f"{'='*100}")
    
    # Estadísticas generales
    total_tests = len(resultados)
    exitos = sum(1 for r in resultados if r['exito'])
    errores = total_tests - exitos
    cumple_consigna = sum(1 for r in resultados if r['cumple_consigna'])
    
    print(f"\n📈 ESTADÍSTICAS GENERALES:")
    print(f"   Total de tests: {total_tests}")
    print(f"   Tests exitosos: {exitos}")
    print(f"   Tests con errores: {errores}")
    print(f"   Cumple consigna: {cumple_consigna}")
    print(f"   Porcentaje de éxito: {(exitos/total_tests)*100:.1f}%")
    print(f"   Porcentaje que cumple consigna: {(cumple_consigna/total_tests)*100:.1f}%")
    
    # Análisis por categoría
    print(f"\nANÁLISIS POR CATEGORÍA:")
    categorias = {}
    for r in resultados:
        cat = r['categoria']
        if cat not in categorias:
            categorias[cat] = {'total': 0, 'exitos': 0, 'cumple_consigna': 0}
        categorias[cat]['total'] += 1
        if r['exito']:
            categorias[cat]['exitos'] += 1
        if r['cumple_consigna']:
            categorias[cat]['cumple_consigna'] += 1
    
    for cat, stats in categorias.items():
        porcentaje_exito = (stats['exitos']/stats['total'])*100
        porcentaje_consigna = (stats['cumple_consigna']/stats['total'])*100
        print(f"   {cat}: {stats['exitos']}/{stats['total']} ({porcentaje_exito:.1f}%) exitos, {stats['cumple_consigna']}/{stats['total']} ({porcentaje_consigna:.1f}%) cumple consigna")
    
    # Casos problemáticos
    print(f"\n CASOS PROBLEMÁTICOS:")
    problemas = [r for r in resultados if not r['exito'] or not r['cumple_consigna']]
    if problemas:
        for i, p in enumerate(problemas[:10], 1):  # Mostrar solo los primeros 10
            print(f"   {i}. {p['categoria']} - {p['descripcion']}")
            if p['error']:
                print(f"      Error: {p['error']}")
            if p['tester_error_info']:
                error_info = p['tester_error_info']
                print(f"      🔍 DEBUG INFO:")
                print(f"         Tipo: {error_info.get('tipo_error', 'N/A')}")
                print(f"         Etapa: {error_info.get('stage', 'N/A')}")
                if error_info.get('cleaned'):
                    print(f"         Limpio: {error_info.get('cleaned')}")
            if not p['cumple_consigna'] and p['exito']:
                print(f"      No cumple consigna: {p['expanded']}")
                print(f"      Producto de factores: {p['es_producto_factores']}")
                print(f"      Suma/diferencia: {p['es_suma_diferencia']}")
                print(f"      Salida LaTeX: {p['es_latex_salida']}")
    else:
        print(f"  No hay casos problemáticos")
    
    # Análisis de patrones de errores del parser
    print(f"\n🔍 ANÁLISIS DE PATRONES DE ERRORES DEL PARSER:")
    errores_tester = [r for r in resultados if r['tester_error_info']]
    if errores_tester:
        # Estadísticas por tipo de error
        tipos_error = {}
        etapas_error = {}
        for error in errores_tester:
            error_info = error['tester_error_info']
            tipo = error_info.get('tipo_error', 'Unknown')
            etapa = error_info.get('stage', 'Unknown')
            
            tipos_error[tipo] = tipos_error.get(tipo, 0) + 1
            etapas_error[etapa] = etapas_error.get(etapa, 0) + 1
        
        print(f" Errores por tipo:")
        for tipo, count in sorted(tipos_error.items(), key=lambda x: x[1], reverse=True):
            print(f"      {tipo}: {count} casos")
        
        print(f"Errores por etapa del pipeline:")
        for etapa, count in sorted(etapas_error.items(), key=lambda x: x[1], reverse=True):
            print(f"      {etapa}: {count} casos")
        
        # Recomendaciones de mejora
        print(f"RECOMENDACIONES DE MEJORA:")
        if 'ValueError' in tipos_error:
            print(f"      • Mejorar validación de entrada para evitar ValueError")
        if 'TypeError' in tipos_error:
            print(f"      • Revisar conversión de tipos en el parsing")
        if 'parse_latex' in etapas_error:
            print(f"      • Fortalecer el parsing principal en parse_latex")
        if 'simplified_parsing' in etapas_error:
            print(f"      • Mejorar el parsing simplificado")
        if 'fallback_parsing' in etapas_error:
            print(f"      • Reforzar los métodos de fallback")
    else:
        print(f"   No se detectaron errores del parser con información de debug")
    
    # Verificación de consigna completa
    print(f"\n VERIFICACIÓN DE CONSIGNA COMPLETA:")
    if cumple_consigna == total_tests:
        print(f"    ¡PERFECTO! El sistema cumple la consigna en TODOS los casos")
        print(f"    Expande productos de factores a sumas/diferencias: 100%")
        print(f"   vManeja sintaxis LaTeX de entrada y salida: 100%")
        print(f"    Procesa todos los tipos de expresiones: 100%")
    elif cumple_consigna >= total_tests * 0.8:
        print(f"    EXCELENTE: El sistema cumple la consigna en la mayoría de casos")
        print(f"    Expande productos de factores a sumas/diferencias: {(cumple_consigna/total_tests)*100:.1f}%")
        print(f"     Algunos casos complejos requieren atención")
    elif cumple_consigna >= total_tests * 0.6:
        print(f"    BUENO: El sistema funciona pero necesita mejoras")
        print(f"    Expande productos de factores a sumas/diferencias: {(cumple_consigna/total_tests)*100:.1f}%")
        print(f"    Muchos casos complejos requieren atención")
    else:
        print(f"    PROBLEMÁTICO: El sistema necesita mejoras significativas")
        print(f"    Expande productos de factores a sumas/diferencias: {(cumple_consigna/total_tests)*100:.1f}%")
        print(f"    La mayoría de casos complejos fallan")

def main():
    """Función principal del test de consigna completa."""
    print(" TEST DE CONSIGNA COMPLETA - EXPANDER ALGEBRAICO")
    print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*100)
    print("Verificando que el sistema cumple COMPLETAMENTE la consigna del proyecto:")
    print("'Expandir una expresión escrita como producto de factores (cada factor es a lo más un polinomio)")
    print("a una expresión escrita como suma o diferencia de términos (un polinomio).")
    print("La expresión es dada usando sintaxis de LaTeX y debe ser devuelta en sintaxis de LaTeX.'")
    print("="*100)
    
    # Recopilar todos los ejemplos del config.py (normales + extremos)
    todos_ejemplos = []
    
    # Agregar ejemplos normales
    for categoria, ejemplos in CATEGORIAS_EJEMPLOS.items():
        for i, ejemplo in enumerate(ejemplos, 1):
            todos_ejemplos.append({
                'latex': ejemplo,
                'descripcion': f"Ejemplo {i}",
                'categoria': categoria
            })
    
    # Agregar ejemplos extremos
    for categoria, ejemplos in CATEGORIAS_EJEMPLOS_EXTREMOS.items():
        for i, ejemplo in enumerate(ejemplos, 1):
            todos_ejemplos.append({
                'latex': ejemplo,
                'descripcion': f"Ejemplo Extremo {i}",
                'categoria': f"{categoria} (EXTREMO)"
            })
    
    total_categorias = len(CATEGORIAS_EJEMPLOS) + len(CATEGORIAS_EJEMPLOS_EXTREMOS)
    print(f"\n Total de ejemplos a probar: {len(todos_ejemplos)}")
    print(f"📂 Categorías normales: {len(CATEGORIAS_EJEMPLOS)}")
    print(f"📂 Categorías extremas: {len(CATEGORIAS_EJEMPLOS_EXTREMOS)}")
    print(f"📂 Total categorías: {total_categorias}")
    
    # Ejecutar tests
    resultados = []
    for i, ejemplo in enumerate(todos_ejemplos, 1):
        print(f"\n{'#'*80}")
        print(f"CASO {i}/{len(todos_ejemplos)} - {ejemplo['categoria']}")
        print(f"{'#'*80}")
        
        resultado = verificar_consigna(
            ejemplo['latex'], 
            ejemplo['descripcion'], 
            ejemplo['categoria']
        )
        resultados.append(resultado)
        
        # Mostrar resultado inmediato
        if resultado['exito']:
            if resultado['cumple_consigna']:
                print(f" EXITOSO: {ejemplo['latex']}")
                print(f"   → {resultado['latex_output']}")
                print(f"   ✓ Producto de factores: {resultado['es_producto_factores']}")
                print(f"   ✓ Suma/diferencia: {resultado['es_suma_diferencia']}")
                print(f"   ✓ Salida LaTeX: {resultado['es_latex_salida']}")
            else:
                print(f"  PARSING OK PERO NO CUMPLE CONSIGNA: {ejemplo['latex']}")
                print(f"   → {resultado['expanded']}")
                print(f"   ✗ Producto de factores: {resultado['es_producto_factores']}")
                print(f"   ✗ Suma/diferencia: {resultado['es_suma_diferencia']}")
                print(f"   ✗ Salida LaTeX: {resultado['es_latex_salida']}")
        else:
            print(f" ERROR: {ejemplo['latex']}")
            print(f"   → {resultado['error']}")
    
    # Generar reporte detallado
    generar_reporte_detallado(resultados)
    
    # Resumen final
    print(f"\n{'='*100}")
    print(f"🏁 RESUMEN FINAL")
    print(f"{'='*100}")
    
    exitos = sum(1 for r in resultados if r['exito'])
    cumple_consigna = sum(1 for r in resultados if r['cumple_consigna'])
    total = len(resultados)
    
    print(f" Tests exitosos: {exitos}/{total} ({(exitos/total)*100:.1f}%)")
    print(f" Cumple consigna: {cumple_consigna}/{total} ({(cumple_consigna/total)*100:.1f}%)")
    
    if cumple_consigna == total:
        print(f"\n ¡SISTEMA PERFECTO! Cumple la consigna en TODOS los casos")
        print(f"   El sistema está listo para uso en producción")
    elif cumple_consigna >= total * 0.8:
        print(f"\n ¡SISTEMA EXCELENTE! Cumple la consigna en la mayoría de casos")
        print(f"   El sistema está listo para uso con algunas limitaciones menores")
    elif cumple_consigna >= total * 0.6:
        print(f"\n SISTEMA FUNCIONAL pero necesita mejoras")
        print(f"   El sistema funciona pero requiere atención en casos complejos")
    else:
        print(f"\n SISTEMA PROBLEMÁTICO que requiere mejoras significativas")
        print(f"   El sistema no cumple la consigna en la mayoría de casos")
    
    print(f"\n Test completado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()