# ExpaAlgebraico v1.0.0 - Desarrollado por Gabriel Bustos (Universidad Nacional de Colombia, 2025)
# Exportador de expresiones SymPy a LaTeX compatible con matplotlib y PDF

from sympy import latex
import os
import subprocess
from input_parser import postprocess_latex_for_display

class LatexExporter:
    @staticmethod
    def to_latex(expr):
        """
        Convierte una expresión sympy a su representación en LaTeX usando pattern matching.
        """
        match expr:
            case None:
                return ""
            case _ if hasattr(expr, 'is_constant') and expr.is_constant:
                latex_code = latex(expr)
            case _ if hasattr(expr, 'is_symbol') and expr.is_symbol:
                latex_code = latex(expr)
            case _:
                latex_code = latex(expr)
        # Postprocesar para hacer compatible con matplotlib
        latex_code = postprocess_latex_for_display(latex_code)
        
        # Restaurar tokens protegidos antes de la salida final
        latex_code = LatexExporter._restaurar_tokens_protegidos(latex_code)
        
        return latex_code

    @staticmethod
    def _restaurar_tokens_protegidos(latex_code: str) -> str:
        """
        Restaura los tokens protegidos a sus comandos LaTeX originales.
        
        Args:
            latex_code: Código LaTeX con tokens protegidos
            
        Returns:
            str: Código LaTeX con tokens restaurados
        """
        # Mapeo inverso de tokens protegidos a comandos LaTeX
        token_mapping = {
            '__PROT__FRAC__': r'\frac',
            '__PROT__SIN__': r'\sin',
            '__PROT__COS__': r'\cos',
            '__PROT__TAN__': r'\tan',
            '__PROT__COT__': r'\cot',
            '__PROT__SEC__': r'\sec',
            '__PROT__CSC__': r'\csc',
            '__PROT__LOG__': r'\log',
            '__PROT__LN__': r'\ln',
            '__PROT__SUM__': r'\sum',
            '__PROT__INT__': r'\int',
            '__PROT__LIM__': r'\lim',
            '__PROT__ALPHA__': r'\alpha',
            '__PROT__BETA__': r'\beta',
            '__PROT__GAMMA__': r'\gamma',
            '__PROT__DELTA__': r'\delta',
            '__PROT__EPSILON__': r'\epsilon',
            '__PROT__ZETA__': r'\zeta',
            '__PROT__ETA__': r'\eta',
            '__PROT__THETA__': r'\theta',
            '__PROT__IOTA__': r'\iota',
            '__PROT__KAPPA__': r'\kappa',
            '__PROT__LAMBDA__': r'\lambda',
            '__PROT__MU__': r'\mu',
            '__PROT__NU__': r'\nu',
            '__PROT__XI__': r'\xi',
            '__PROT__OMICRON__': r'\omicron',
            '__PROT__PI__': r'\pi',
            '__PROT__RHO__': r'\rho',
            '__PROT__SIGMA__': r'\sigma',
            '__PROT__TAU__': r'\tau',
            '__PROT__UPSILON__': r'\upsilon',
            '__PROT__PHI__': r'\phi',
            '__PROT__CHI__': r'\chi',
            '__PROT__PSI__': r'\psi',
            '__PROT__OMEGA__': r'\omega',
            '__PROT__LEFT__': r'\left',
            '__PROT__RIGHT__': r'\right',
        }
        
        # Restaurar tokens protegidos
        for token, command in token_mapping.items():
            latex_code = latex_code.replace(token, command)
        
        return latex_code

    @staticmethod
    def export_latex_to_pdf(latex_code: str, output_path: str) -> dict:
        """
        Exporta un código LaTeX matemático a un archivo PDF usando pdflatex con pattern matching.
        Args:
            latex_code (str): El código LaTeX matemático (sin encabezado de documento).
            output_path (str): Ruta donde se guardará el PDF (debe terminar en .pdf).
        Returns:
            dict: {'success': True/False, 'error': mensaje de error si falla}
        """
        # Validar entrada usando pattern matching
        match output_path:
            case path if not path.endswith('.pdf'):
                return {'success': False, 'error': 'La ruta debe terminar en .pdf'}
            case path if not path or not path.strip():
                return {'success': False, 'error': 'Ruta de salida no válida'}
            case _:
                pass
        match latex_code:
            case None | "":
                return {'success': False, 'error': 'Código LaTeX vacío'}
            case code if not code.strip():
                return {'success': False, 'error': 'Código LaTeX vacío'}
            case code if len(code) > 10000:
                return {'success': False, 'error': 'Código LaTeX demasiado largo (máximo 10000 caracteres)'}
            case _:
                pass
        # Crear el archivo .tex temporal en la misma carpeta que el PDF
        tex_path = os.path.splitext(output_path)[0] + '.tex'
        # Estructura básica de un documento LaTeX
        tex_content = (
            "\\documentclass{article}\n"
            "\\usepackage{amsmath}\n"
            "\\begin{document}\n"
            "\\[\n"
            f"{latex_code}\n"
            "\\]\n"
            "\\end{document}\n"
        )
        try:
            # Guardar el archivo .tex
            with open(tex_path, "w", encoding="utf-8") as f:
                f.write(tex_content)
            # Compilar a PDF usando pdflatex
            pdf_dir = os.path.dirname(tex_path)
            cmd = f'pdflatex -interaction=nonstopmode -output-directory "{pdf_dir}" "{tex_path}"'
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            match result.returncode:
                case 0:
                    return {'success': True, 'error': None}
                case _:
                    return {'success': False, 'error': result.stderr}
        except Exception as e:
            match e:
                case FileNotFoundError():
                    return {'success': False, 'error': 'pdflatex no encontrado. Instala LaTeX para continuar.'}
                case PermissionError():
                    return {'success': False, 'error': 'Error de permisos al escribir el archivo.'}
                case _:
                    return {'success': False, 'error': str(e)}