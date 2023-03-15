from sympy import symbols
from sympy.stats import Poisson, density
from sympy.stats import E, variance

lam = symbols('lambda')
lam = 0.5

X = Poisson('X', lam)

print(E(X))
print(variance(X))

