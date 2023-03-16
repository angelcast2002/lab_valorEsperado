from sympy import symbols, exp, diff, EulerGamma
from sympy.stats import Poisson, E, variance

lam = symbols('lambda')
lam = 0.5
euler = EulerGamma.evalf()
s = symbols('s')

X = Poisson('X', lam)

print(E(X))
print(variance(X))


funGeneradoraMomentos = E(exp(s*X))

valorEsperado = funGeneradoraMomentos.diff(s).subs(s, 0)
print(valorEsperado)

#Teorema 9
varianza = funGeneradoraMomentos.diff(s, 2).subs(s, 0) - valorEsperado**2
print(varianza)