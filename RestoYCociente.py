print("Ingrese los numero requeridos para realizar la division")
dividendo = int(input("Ingrese por favor un numero entero: "))
divisor = int(input("Ingrese por facor otro numero entero: "))
if divisor>0 :
    cociente = dividendo / divisor
    resto = dividendo % divisor
    print ("El cociente de la division es ", cociente," y el resto es ","%.2f" % resto)
else:
    print("ERROr, no se puede dividir un numero entre 0")
