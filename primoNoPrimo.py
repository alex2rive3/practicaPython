def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True
numero = int(input("Ingrese un numero por favor: "))
es_primo(numero)
input()