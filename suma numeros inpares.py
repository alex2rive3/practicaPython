numero = 20
acumulador =0
if numero%2==0:
    numero = numero-1
    for x in range(numero,0,-2):
        print(x)
        acumulador += x
else:
    for x in range (numero,0,-2):
        print(x)
        acumulador += x
print("La suma de los n primeros numeros impares es ", acumulador)
input()