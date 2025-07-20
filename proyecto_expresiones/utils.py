#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Utilidades para ExpaAlgebraico
Funciones auxiliares que no pertenecen al parser principal
"""

from typing import Optional

def identificar_categoria_pedagogica(expr: str, categorias_ejemplos: dict) -> Optional[str]:
    """
    Identifica la categoría pedagógica de una expresión según las categorías proporcionadas.
    
    Args:
        expr (str): Expresión a categorizar
        categorias_ejemplos (dict): Diccionario con categorías y ejemplos
        
    Returns:
        Optional[str]: Categoría encontrada o None si no se encuentra
    """
    expr_normalizado = expr.strip().replace(' ', '').replace('\n', '').replace(r'\left', '').replace(r'\right', '')
    
    for categoria, ejemplos in categorias_ejemplos.items():
        for ejemplo in ejemplos:
            ejemplo_normalizado = ejemplo.strip().replace(' ', '').replace('\n', '').replace(r'\left', '').replace(r'\right', '')
            
            # Coincidencia exacta
            if expr == ejemplo:
                return categoria
                
            # Coincidencia normalizada
            if expr_normalizado == ejemplo_normalizado:
                return categoria
                
            # Coincidencia parcial básica
            if expr_normalizado in ejemplo_normalizado or ejemplo_normalizado in expr_normalizado:
                return categoria
                
    return None