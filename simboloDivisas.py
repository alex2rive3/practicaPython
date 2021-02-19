diccionario = {'Euro':'€', 'Dolar':'$', 'Yen':'¥'}
divisa = input("Introduce una divisa: ")
#get es para buscar el key en el diccionario si encuentra devuelve el valor o de lo contrario no devuelve nada
print(diccionario.get(divisa.title(), "La divisa no está."))