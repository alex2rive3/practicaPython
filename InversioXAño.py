inversion = int(input("ingrese el monto que le gustaria invertir: "))
interes = float(input("ingrese el interes anual de la inversion: "))
anhos = int(input("ingrese los años de inversion previstos: "))
for x in range(1, anhos+1):
    print("su ganancia en el año ", x ," es de ", (inversion*interes*x))
input()