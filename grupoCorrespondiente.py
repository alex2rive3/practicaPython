nombre = input("Cual es su nombre?? ")
sexo = str(input("Cual es su sexo?? Ingrese M si es masculino o F si es femenino ")).lower()
primeraLetraNombre = nombre[0].upper()
if ( sexo == "f" and primeraLetraNombre < "M") or ( sexo == "m" and primeraLetraNombre > "N"):
    print("Estas en el Grupo A")
else:
    print("Estas en el Grupo B")