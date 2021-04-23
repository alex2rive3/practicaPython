from sympy import *
x = symbols('x')
polinomio1 = poly(6 * x ** 2 + 7 * x - 5)
polinomio2 = poly(x ** 2 - 5 * x + 6)
resta = polinomio1 - polinomio2
print(resta)