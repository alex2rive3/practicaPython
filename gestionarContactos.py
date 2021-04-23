import itertools
doc=open('contactos.txt','r+')
def listar():
    lineas = doc.readlines()
    for fila in lineas:
        print (fila)
def agregar():
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el numero del contacto: ")
    doc.write(nombre + " " + numero + "\n")
def consultar():
    lista = []
    nombre = input("Ingrese el nombre de conbtacto a buscar: ")
    rows = doc.readlines()
    for fila in rows:
        lista.append(fila.split())
    diccionario = dict(lista)
    for key in diccionario:
        if (nombre == key):
            mensaje = "El numero de telefono de " + nombre + " es " + diccionario[key]
            break
        else:
            mensaje = "El contacto que busca no existe"
    print(mensaje)
def eliminar():
    lineas = doc.readlines()
    nombre = input("Escriba el nombre del contacto a eliminar:")
    for linea in lineas: 
        if linea.strip("\n") != nombre:
            doc.write(linea)

print ("que deceras realizar:")
print("""Menu 
1. agregar
2. consultar
3. eliminar
4. listar
5. salir""")
opcion = int(input("Ingrese su opcion: "))
if opcion == 1: agregar()
elif opcion ==2: consultar()
elif opcion == 3: eliminar()
elif opcion == 4: listar()
#elif opcion == 5: break