#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Parche para latex2sympy2 que soluciona el problema de typing.io en Python 3.12+
"""

import sys
import importlib.util
import logging

logger = logging.getLogger(__name__)

def patch_latex2sympy():
    """
    Aplica un parche a latex2sympy2 para hacerlo compatible con Python 3.12+
    """
    try:
        # Verificar si typing.io existe
        try:
            import typing.io
            # Si no hay error, no necesitamos el parche
            return True
        except ImportError:
            # Necesitamos aplicar el parche
            pass
        
        # Crear un módulo typing.io falso
        import types
        import typing
        
        # Crear el submódulo io
        io_module = types.ModuleType('typing.io')
        
        # Definir TextIO y BinaryIO
        class TextIO:
            pass
        
        class BinaryIO:
            pass
        
        # Agregar las clases al módulo
        io_module.TextIO = TextIO
        io_module.BinaryIO = BinaryIO
        
        # Agregar el módulo al sistema
        sys.modules['typing.io'] = io_module
        
        # Agregar el submódulo a typing
        typing.io = io_module
        
        # Verificar que latex2sympy2 ahora funciona
        try:
            import latex2sympy2
            logger.info("Parche aplicado correctamente a latex2sympy2")
            return True
        except ImportError as e:
            logger.error(f"No se pudo importar latex2sympy2 después del parche: {e}")
            return False
    except Exception as e:
        logger.error(f"Error al aplicar el parche a latex2sympy2: {e}")
        return False

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    patch_latex2sympy()