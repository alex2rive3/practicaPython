from sympy import *  
#Definimos los simbolos a utilizar 
x = symbols('x')
p1 = 2 * x ** 3 + 5*x - 3
p2 = 2 * x ** 3 - 3 * x ** 2 + 4
#las variables pasan a convertirse en polinomios 
PrimerPolinomio = Poly(p1)
SeguntoPolinomio = Poly(p2)
#se realiza la suma de ambos polinomios 
suma = PrimerPolinomio + SeguntoPolinomio
print(suma)