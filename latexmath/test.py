"""  conda install -c anaconda sympy """
 
import sympy as sym
import sympy.printing as printing
string = sym.symbols('Delta__y_l')
print(printing.latex(string))