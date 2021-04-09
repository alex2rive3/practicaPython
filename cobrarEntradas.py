edad = int(input("Ingrese su edad por favor: "))
if edad <=4:
    print("Puedes pasar gratis")
elif edad > 4 and edad <=17:
    print("Debe abonar 5 euros para poder entrar")
elif edad >= 18:
    print("Debe abonar 10 euros para poder entrar")
input()