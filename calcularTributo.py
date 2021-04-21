print("Bienvenido!!!")
print("Proporciones los datos e ingresos mensuales para saber si debe pagar el impuesto o no")
edad = int(input("Cual es su edad? "))
ingresos = float(input("Cual es su ingreso mensual? "))
if (edad > 16 and ingresos > 1000):
    print("Usted ya debe tributar")
else:
    print("Usted aun se esta salbando de tributar!!")