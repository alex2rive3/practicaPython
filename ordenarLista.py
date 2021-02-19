def ordenamientoBurbuja(unaLista):
    #el for rrecorre de atras para delante la lista 
    #rrecorre la longitud menos 1
    for numPasada in range(len(unaLista)-1,0,-1):
        #este for itera i hasta llegar al numero pasado por el for anterior
        for i in range(numPasada):
            #pregunta si lo que esta en la posision i es mayor que lo que esta en i+1 (osea en la siguiente casilla)
            if unaLista[i]>unaLista[i+1]:
                #si la sentencia anterior es verdadera se realiza el cambio
                #lo que hay en unaLista[i] se pasa temporalemte a temp
                temp = unaLista[i]
                #ahora unaLista[i] ya tendra el valor de la siguient casilla
                unaLista[i] = unaLista[i+1]
                #y se asigna a la casilla siguient el valor de temp 
                unaLista[i+1] = temp
    print(unaLista)
numGanadores = []
for x in range(0,8):
    numGanadores.append(int(input("Escriba los numeros ganadores de la loteria: ")))
ordenamientoBurbuja(numGanadores)
input()
