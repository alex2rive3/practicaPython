def factorial(num):
    fact = 1
    for x in range(1, num+1):
        fact = fact*x
    return fact
numero = int(input("Escriba el numero para calcula el factorial: "))
print("el factorial del numero es: ", factorial(numero))