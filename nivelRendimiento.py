rendimiento = float(input("ingrese la puntuacion del empleado: "))
if rendimiento == 0.0:
    print("Su nivel de rendimiento es Inaceptable y por eso has ganado", (rendimiento*2400), "euros")
elif rendimiento == 0.4:
    print("Su nivel de rendimiento es Aceptable y por eso has ganado", (rendimiento*2400), "euros")
elif rendimiento >= 0.6:
    print("Su nivel de rendimiento es Meritorio y por eso has ganado", (rendimiento*2400), "euros")
input()