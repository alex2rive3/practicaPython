diccionario = {}
documento = open("socios.txt","r+")
print("Registrar nuevo socio")
repetir = 0
print("Ingrese el numero 1 para para dejar de agregar socios: ")
while (repetir == 0):
    numero= input("Ingrese el numero de socio: ")
    nombre = input("Ingrese el nombre del socio: ")
    apellido = input("Ingrese el apellido del socio: ")
    fecha = input("Ingrese la fecha de hoy en el siguiente formato dd-mm-aaaa: ")
    diccionario [numero] = nombre, apellido, fecha
    for num, socio in diccionario.items():
        documento.write(num + ") ")
        for datos in socio:
            documento.write(datos + " ")
    documento.write("\n")
    repetir = int(input("Ingrese 0 para agregar un socio nuevo: "))
documento.close()