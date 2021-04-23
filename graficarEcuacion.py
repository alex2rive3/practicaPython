from matplotlib import pyplot
from sympy import *
def ecuacion1(x):
    return 2 * (x ** 2) - 2 * x - 3
def ecuacion2(x):
    return 4 * x + 1
#valores para el eje X
x = range(-10, 15)
#GRAFICA AMBAS FUNCIONES 
pyplot.plot(x, [ecuacion1(i) for i in x])
pyplot.plot(x, [ecuacion2(i) for i in x])

##Establecer el color de los ejes 
pyplot.axhline(0, color="black") #LINEA X
pyplot.axvline(0, color="black") #LINEA Y

#LIMITAR LOS VALORES DE LOS EJES 
pyplot.xlim(10, -10)
pyplot.ylim(10, -10)

#GUARDAR GRAFICOS COMO UNA IMAGEN 
pyplot.savefig("Grafico.png")

pyplot.show()