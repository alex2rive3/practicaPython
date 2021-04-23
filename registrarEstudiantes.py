alumnos = {}
documento = open('datoEstudiantes.txt', 'r+')
print("Registrar nuevo Alumno")
for x in range(1,11):
    nombre = input("Escriba el nombre del alumno: ")
    apellido = input("Escriba el apellido del alumno: ")
    edad = int(input("Ingre la edad del alumno: "))
    lugarDeNacimiento = input("Ingrese el lugar del nacimiento del alumno: ")
    nacionalidad = input("Ingrese la nacionalidad del alumno: ")
    #convertir entero a string para poder escribir en el fichero
    edad = str(edad)
    numeroDeRegistro = str(x)
    documento.write(numeroDeRegistro + " " + nombre + " " + apellido + " " + edad + " " + lugarDeNacimiento + " " + nacionalidad + "\n")
documento.close()