print("Bienvenido!!!")
renta = int(input("ingrese su renta anual por favor: "))
if renta < 10000:
    print("la renta impositiva que te corresponde es del 5%")
elif renta > 10000 and renta < 20000:
    print("la renta impositiva que te corresponde es del 15%")
elif renta>20000 and renta < 35000:
    print("la renta impositiva que te corresponde es del 20%")
elif renta > 35000 and renta<60000:
    print("la renta impositiva que te corresponde es del 30 %")
elif renta > 60000:
    print("la renta impositiva que te corresponde es del 45%")
input()