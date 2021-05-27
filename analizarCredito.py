print("--------------------------Bienvenido  al Banco de Tus Sueños---------------------------")
print("Por favor proporcione los datos requeridos para analizar si puede accedera a un credito")
edad = int(input("Cuantos años tienes?? "))
ingresos = float(input("cual es su ingreso mensual??"))
antiguedadLaboral = float(input("Ingrese su antiguedad laboral en años por favor "))
if (edad > 18 and edad < 65):
    if(antiguedadLaboral > 1):
        if (ingresos > 1500000 and ingresos < 3000000):
            print("Puedes acceder a un credito de hasta 3.000.000 Gs")
        elif(ingresos > 3000000 and ingresos <5000000):
            print("Puedes acceder a creditos de hasta 15.000.000 Gs")
    else:
        print("Debes tener mas de un año de antiguedad laborar para acceder a un credito")
else:
    print("No se encuantra en el rango de edad apto para un credito:")
