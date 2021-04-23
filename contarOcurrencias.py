diccionario = { "a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0, "ñ":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0}
repetidor = 0
listaPalabras = []
while repetidor < 10: 
    repetidor +=1
    palabras = input("Ingrese un String: ",repetidor)
    listaPalabras.append(palabras)
for datos in listaPalabras:
    if datos not in diccionario:
        diccionario[datos]=0
    else: 
        diccionario[datos]+=1
print("String contados: ")
for key, val in diccionario.items():
    print(key, " : ", val)