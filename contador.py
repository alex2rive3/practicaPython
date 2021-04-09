frase = str(input("Escriba una frase por favor: "))
caracter = str(input("Ingrese una letra: "))
contador = 0
for x in frase:
    if x == caracter:
        contador = contador + 1
print("la letra (", caracter, ") aparece en la frase en ", contador, " ocacion/es")
input()