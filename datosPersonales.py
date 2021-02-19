diccionario = {"nombre":" ", "telefono":" ", "edad":" ", "direccion":" "}
diccionario["nombre"] = input("Cual es tu nombre? ")
diccionario["edad"] = int(input("Cuantos años tienes? "))
diccionario["telefono"] = int(input("Cual es tu numero de telefono? "))
diccionario["direccion"] = str(input("Cual es la direccion de donde vives? "))
print(diccionario.get("nombre"), " tiene ", diccionario.get("edad"), " años, vive en ", diccionario.get("direccion"), " y su numero de telefono es ", diccionario.get("telefono"))
