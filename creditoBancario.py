def datosNecesarios():
    global edad, salario, credito, cuota, totalAPagar, montoCuota
    edad = int(input("Ingrese Su Edad: "))
    salario = float(input("Ingrese su salario Mensual: "))
    credito  = float(input("Cual es el monto del credito que decea: "))
    cuota = int(input("En cuantas cuotas decea pagarlos: "))
    return edad, salario, credito, cuota

def creditosPersonales(salario, credito, cuota):
    montoCuota = 0
    totalAPagar = 0
    if(cuota > 0 and cuota < 12):
        totalAPagar = credito + ((credito / 1000000)* 97000)
        montoCuota = totalAPagar / cuota
        if( montoCuota < salario * 0.30):
            print("El monto total a pagar es {:,.0f}".format(totalAPagar),  " y la cuota mensual sera de {:,.0f}".format(montoCuota))
        else: 
            print("El monto total de su cuota no debe ecceder el 30 porciento de su salario")
    elif(cuota > 12 and cuota < 18):
        totalAPagar = credito + ((credito / 1000000)* 69000)
        montoCuota = totalAPagar / cuota
        if( montoCuota < salario * 0.30):
            print("El monto total a pagar es {:,.0f}".format(totalAPagar),  " y la cuota mensual sera de {:,.0f}".format(montoCuota))
        else: 
            print("El monto total de su cuota no debe ecceder el 30 porciento de su salario")
    elif(cuota > 18 and cuota < 24):
        totalAPagar = credito + ((credito / 1000000)* 56000)
        montoCuota = totalAPagar / cuota
        if( montoCuota < salario * 0.30):
            print("El monto total a pagar es {:,.0f}".format(totalAPagar),  " y la cuota mensual sera de {:,.0f}".format(montoCuota))
        else: 
            print("El monto total de su cuota no debe ecceder el 30 porciento de su salario")        
    elif(cuota > 24 and cuota < 36):
        totalAPagar = credito + ((credito / 1000000)* 43000)
        montoCuota = totalAPagar / cuota
        if( montoCuota < salario * 0.30):
            print("El monto total a pagar es {:,.0f}".format(totalAPagar),  " y la cuota mensual sera de {:,.0f}".format(montoCuota))
        else: 
            print("El monto total de su cuota no debe ecceder el 30 porciento de su salario")
    elif(cuota > 36 and cuota < 48):
        totalAPagar = credito + ((credito / 1000000)* 36000)
        montoCuota = totalAPagar / cuota
        if( montoCuota < salario * 0.30):
            print("El monto total a pagar es {:,.0f}".format(totalAPagar),  " y la cuota mensual sera de {:,.0f}".format(montoCuota))
        else: 
            print("El monto total de su cuota no debe ecceder el 30 porciento de su salario")
    elif(cuota > 48 and cuota < 60):
        totalAPagar = credito + ((credito / 1000000)* 33000)
        montoCuota = totalAPagar / cuota
        if( montoCuota < salario * 0.30):
            print("El monto total a pagar es {:,.0f}".format(totalAPagar),  " y la cuota mensual sera de {:,.0f}".format(montoCuota))
        else: 
            print("El monto total de su cuota no debe ecceder el 30 porciento de su salario")
    else:
        print("La cantidad de cuotas que decea no esta permitido")

def creditosParaViviendas(salario, credito, cuota):
    if(cuota > 0 and cuota < 18):
        totalAPagar = credito + ((credito / 1000000)* 68000)
        montoCuota = totalAPagar / cuota
        if( montoCuota < salario * 0.30):
            print("El monto total a pagar es {:,.0f}".format(totalAPagar),  " y la cuota mensual sera de {:,.0f}".format(montoCuota))
        else: 
            print("El monto total de su cuota no debe ecceder el 30 porciento de su salario")
    elif(cuota > 18 and cuota < 24):
        totalAPagar = credito + ((credito / 1000000)* 54000)
        montoCuota = totalAPagar / cuota
        if( montoCuota < salario * 0.30):
            print("El monto total a pagar es {:,.0f}".format(totalAPagar),  " y la cuota mensual sera de {:,.0f}".format(montoCuota))
        else: 
            print("El monto total de su cuota no debe ecceder el 30 porciento de su salario")
    elif(cuota > 24 and cuota < 36):
        totalAPagar = credito + ((credito / 1000000)* 39000)
        montoCuota = totalAPagar / cuota
        if( montoCuota < salario * 0.30):
            print("El monto total a pagar es {:,.0f}".format(totalAPagar),  " y la cuota mensual sera de {:,.0f}".format(montoCuota))
        else: 
            print("El monto total de su cuota no debe ecceder el 30 porciento de su salario")        
    elif(cuota > 36 and cuota < 48):
        totalAPagar = credito + ((credito / 1000000)* 32000)
        montoCuota = totalAPagar / cuota
        if( montoCuota < salario * 0.30):
            print("El monto total a pagar es {:,.0f}".format(totalAPagar),  " y la cuota mensual sera de {:,.0f}".format(montoCuota))
        else: 
            print("El monto total de su cuota no debe ecceder el 30 porciento de su salario")
    elif(cuota > 48 and cuota < 60):
        totalAPagar = credito + ((credito / 1000000)* 28000)
        montoCuota = totalAPagar / cuota
        if( montoCuota < salario * 0.30):
            print("El monto total a pagar es {:,.0f}".format(totalAPagar),  " y la cuota mensual sera de {:,.0f}".format(montoCuota))
        else: 
            print("El monto total de su cuota no debe ecceder el 30 porciento de su salario")
    elif(cuota > 60 and cuota < 72):
        totalAPagar = credito + ((credito / 1000000)* 26000)
        montoCuota = totalAPagar / cuota
        if( montoCuota < salario * 0.30):
            print("El monto total a pagar es {:,.0f}".format(totalAPagar),  " y la cuota mensual sera de {:,.0f}".format(montoCuota))
        else: 
            print("El monto total de su cuota no debe ecceder el 30 porciento de su salario")
    elif(cuota > 72 and cuota < 84):
        totalAPagar = credito + ((credito / 1000000)* 24000)
        montoCuota = totalAPagar / cuota
        if( montoCuota < salario * 0.30):
            print("El monto total a pagar es {:,.0f}".format(totalAPagar),  " y la cuota mensual sera de {:,.0f}".format(montoCuota))
        else: 
            print("El monto total de su cuota no debe ecceder el 30 porciento de su salario")
    else:
        print("La cantidad de cuotas que decea no esta permitido")

def creditoParaAhorristas(salario, credito, cuota):
    if(cuota > 0 and cuota < 12):
        totalAPagar = credito + ((credito / 1000000)* 95000)
        montoCuota = totalAPagar / cuota
        if( montoCuota < salario * 0.30):
            print("El monto total a pagar es {:,.0f}".format(totalAPagar),  " y la cuota mensual sera de {:,.0f}".format(montoCuota))
        else: 
            print("El monto total de su cuota no debe ecceder el 30 porciento de su salario")
    elif(cuota > 12 and cuota < 24):
        totalAPagar = credito + ((credito / 1000000)* 53000)
        montoCuota = totalAPagar / cuota
        if( montoCuota < salario * 0.30):
            print("El monto total a pagar es {:,.0f}".format(totalAPagar),  " y la cuota mensual sera de {:,.0f}".format(montoCuota))
        else: 
            print("El monto total de su cuota no debe ecceder el 30 porciento de su salario")
    elif(cuota > 24 and cuota < 36):
        totalAPagar = credito + ((credito / 1000000)* 39000)
        montoCuota = totalAPagar / cuota
        if( montoCuota < salario * 0.30):
            print("El monto total a pagar es {:,.0f}".format(totalAPagar),  " y la cuota mensual sera de {:,.0f}".format(montoCuota))
        else: 
            print("El monto total de su cuota no debe ecceder el 30 porciento de su salario")        
    elif(cuota > 36 and cuota < 60):
        totalAPagar = credito + ((credito / 1000000)* 29000)
        montoCuota = totalAPagar / cuota
        if( montoCuota < salario * 0.30):
            print("El monto total a pagar es {:,.0f}".format(totalAPagar),  " y la cuota mensual sera de {:,.0f}".format(montoCuota))
        else: 
            print("El monto total de su cuota no debe ecceder el 30 porciento de su salario")
    else:
        print("La cantidad de cuotas que decea no esta permitido")

def menu():
    print("""*************** Bienvenido al Banco de tus Sueños ***************
    Seleccione la Opcion del Credito que decea Gestionar
    1- Creditos Personales
    2- Creditos para Ahorristas
    3- creditos para Viviendas
    0- Salir""")


menu()
opcion = int(input("ingrese la opcion que prefiere: "))
while(opcion > 0):
    datosNecesarios()
    if (edad > 18 and edad < 60):
        if opcion == 1:
            creditosPersonales(salario, credito, cuota)
            menu()
            opcion = int(input("Ingrese otra opcion si decea gestionar otro credito o ingrese 0 para salir: "))
        elif opcion == 2:
            #datosNecesarios()
            creditoParaAhorristas(salario, credito, cuota)
            menu()
            opcion = int(input("Ingrese otra opcion si decea gestionar otro credito o ingrese 0 para salir: "))
        elif opcion == 3:
            #datosNecesarios()
            creditosParaViviendas(salario, credito, cuota)
            menu()
            opcion = int(input("Ingrese otra opcion si decea gestionar otro credito o ingrese 0 para salir: "))
        elif opcion == 0:
            break
        else:
            print("Opcion no valida")
    else:
        print("Lo siento necesariamente debes ser mayor de edad para acceder a un credito")
        break
