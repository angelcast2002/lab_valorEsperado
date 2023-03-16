from sympy import symbols, exp, diff, EulerGamma
from sympy.stats import Poisson, E, variance

#Se define lambda y se da su valor
lam = symbols('lambda')
lam = 0.5

#Se obtiene el valor de la constante de euler
euler = EulerGamma.evalf()
s = symbols('s')

X = Poisson('X', lam)


#Valor esperado con la funcion E
print("Valor esperado funcion E:", E(X).evalf())

#Varianza con la funcion variance
print("Varianza funcion variance:", variance(X).evalf())

#Funcion generadora de momentos
funGeneradoraMomentos = E(exp(s*X))

#Valor esperado utilizando la primera derivada de la funcion generadora de momentos
valorEsperado = funGeneradoraMomentos.diff(s).subs(s, 0)
print("Valor esperado, funcion generadora:", valorEsperado.evalf())

#Teorema 9
#Varianza utilizando la segunda derivada de la funcion generadora de momentos
varianza = funGeneradoraMomentos.diff(s, 2).subs(s, 0) - valorEsperado**2
print("Varianza, funcion generadora:", varianza.evalf())