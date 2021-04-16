def ingresar():
    global x,y
    x = float(input("Ingrese el primer numero por favor: "))
    y = float(input("Ingrese el segundo numero por favor: "))
def suma():
    print("la suma es ",x+ y)
def resta():
    print("la resta es ",x-y)
def multi():
    print("El producto es ",x*y)
def divi():
    if(y>0):
        print("El cociente es ",x/y)
    else:
        print("No puedes dividir con 0")
repetir = True
while (repetir):
    print("""************
    Calculadora
    ************
    Menu
    1) Suma
    2) Resta
    3) Multiplicacion
    4) Division
    5) Salir""")
    opcion = int(input("Ingrese la opcion de la Operacion que desea Realizar "))
    if (opcion == 1):
        ingresar()
        suma()
    elif(opcion == 2):
        ingresar()
        resta()
    elif(opcion == 3):
        ingresar()
        multi()
    elif(opcion == 4):
        ingresar()
        divi()
    elif(opcion == 5):
        repetir = False
    else:
        print("Opcion no valida")