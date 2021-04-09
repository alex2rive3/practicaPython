#el usuario debe adivinar el numero secreto
import random
secreto = random.randint(1,20)
intentosPermitidos = 5
intentosRealizados = 1
nombre = input("cual es tu nombre? ")
print(nombre,"Estoy pensando en un numero del 1 al 20 intenta averiguar ")
numero = int(input("Escriba el numero que crea correcto, tienes 5 intentos "))
while intentosRealizados < intentosPermitidos:
    intentosRealizados += 1 
    if secreto > numero:
        numero = int(input("El numero que acabas de ingresar es menor al numero secreto. Intenta de vuelta: "))
    elif secreto < numero:
        numero = int(input("El numero que acabas de ingresar es mayor al numero secreto. Intenta de vuelta: "))
    elif secreto == numero:
        print ("Felicidades ", nombre, "haz adivinado el numero que pensé en el intento numero", intentosRealizados)
        break
if intentosRealizados == intentosPermitidos:
    print("Lamentablemente haz agotado tus oportunidades y no adivinaste el numero secreto :(")