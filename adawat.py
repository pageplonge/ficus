from sympy import *
from lexer import *

class strictForms(Enum):
  MONOMIAL = 'Monomial'
  EXPONENTIAL = 'Exponential'
  POLYNOMIAL = 'Polynomial'
  MULTINOMIAL = 'Multinomial'
  QUADRATIC = 'Quadratic'
  RATIONAL = 'Rational'
  INTEGRAL = 'Integral'
  SUM = 'Sum'
  PRODUCT = 'Product'
  SQRT = 'Sqrt'
  SINUSOIDAL = 'sin'
  COSINUSOIDAL = 'cos'
  TANGENT = 'tan'
  CSC = "csc"
  SEC = 'sec'
  ARCTAN = 'atan'
  BINOMIALTP = 'RaisedBinomial'
  INVERSEBINOMIAL = 'InverseBinomial'
  INVERSEQUADRATIC = 'InverseQuadratic'
  COMPOSITE = 'Composite'
  INVERSEROOT = 'InverseRoot'
  
def fits(expr, form, wrt=False):
  pass
      