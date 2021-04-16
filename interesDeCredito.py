print("Por favor proporciones los datos necesarios para calcular el interes de su credito")
credito = float(input("Cual fue el monto del credito?? "))
tiempo = int(input("Ingrese el plazo del credito en Meses: "))
tasaDeInteres = float(input("Ingrese el porcentaje de interes del credito "))/100
interesTotal = (credito * tasaDeInteres * tiempo)/12
print ("El interes total de su credito asciende a un total de ", interesTotal,"$")