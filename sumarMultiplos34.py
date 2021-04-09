numero = int(input("ingrese un numero: "))
suma = 0
while numero>=0:
    if numero%3 ==0 or numero%4 == 0:
        suma += numero
    elif numero<0:
        break
    numero = int(input("ingrese otro numero: "))
print("la suma de todos los numeros es: ", suma)
