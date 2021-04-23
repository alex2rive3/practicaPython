from sympy import *
x = symbols('x')
y = symbols('y')
p1 = poly (4 * x - 7 * x * y)
p2 = poly (2 * y + 3 * x)
producto = p1 * p2
print(producto)