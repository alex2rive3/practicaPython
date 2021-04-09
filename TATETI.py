#Se carga la matriz con * para poder visualizar el tablero de juego
import random
matriz = [["*","*","*"],
["*","*","*"],
["*","*","*"]]
i=0
def imprimirMatriz():
    for filas in matriz:
        for valor in filas:
            print("\t", valor, end=" ")
        print()
imprimirMatriz()
def ubicarO(num):
    if num == 1:
        if matriz[0][0] == "*":
            matriz[0][0]= "O"
        else:
            num = int(input("este lugar ya esta ocupado prueba con otro: "))
    elif num == 2:
        if matriz[0][1] == "*":
            matriz[0][1]= "O"
        else:
            num = int(input("este lugar ya esta ocupado prueba con otro: "))
    elif num == 3:
        if matriz[0][2] == "*":
            matriz[0][2]= "O"
        else:
            num = int(input("este lugar ya esta ocupado prueba con otro: "))
    elif num == 4:
        if matriz[1][0] == "*":
            matriz[1][0]= "O"
        else:
            num = int(input("este lugar ya esta ocupado prueba con otro: "))
    elif num == 5:
        if matriz[1][1] == "*":
            matriz[1][1]= "O"
        else:
            num = int(input("este lugar ya esta ocupado prueba con otro: "))
    elif num == 6:
        if matriz[1][2] == "*":
            matriz[1][2]= "O"
        else:
            num = int(input("este lugar ya esta ocupado prueba con otro: "))
    elif num == 7:
        if matriz[2][0] == "*":
            matriz[2][0]= "O"
        else:
            num = int(input("este lugar ya esta ocupado prueba con otro: "))
    elif num == 8:
        if matriz[2][1] == "*":
            matriz[2][1]= "O"
        else:
            num = int(input("este lugar ya esta ocupado prueba con otro: "))
    elif num == 9:
        if matriz[2][2] == "*":
            matriz[2][2]= "O"
        else:
            num = int(input("este lugar ya esta ocupado prueba con otro: "))
def ubicarX(num):
    if jugadorX == 1:
        if matriz[0][0] == "*":
            matriz[0][0]= "X"
    elif jugadorX == 2:
        if matriz[0][1] == "*":
            matriz[0][1]= "X"
    elif jugadorX == 3:
        if matriz[0][2] == "*":
            matriz[0][2]= "X"
    elif jugadorX == 4:
        if matriz[1][0] == "*":
            matriz[1][0]= "X"
    elif jugadorX == 5:
        if matriz[1][1] == "*":
            matriz[1][1]= "X"
    elif jugadorX == 6:
        if matriz[1][2] == "*":
            matriz[1][2]= "X"
    elif jugadorX == 7:
        if matriz[2][0] == "*":
            matriz[2][0]= "X"
    elif jugadorX == 8:
        if matriz[2][1] == "*":
            matriz[2][1]= "X"
    elif jugadorX == 9:
        if matriz[2][2] == "*":
            matriz[2][2]= "X"
def ganaJugadorO():
    if matriz[0][0] == "O" and matriz[0][1] == "O" and matriz[0][2] == "O":
        print("Gana el jugador O")
    elif matriz[1][0] == "O" and matriz[1][1] == "O" and matriz[1][2] == "O":
        print("Gana el jugador O")
    elif matriz[2][0] == "O" and matriz[2][1] == "O" and matriz[2][2] == "O":
        print("Gana el jugador O")
    elif matriz[0][0] == "O" and matriz[1][0] == "O" and matriz[2][0] == "O":
        print("Gana el jugador O")
    elif matriz[0][1] == "O" and matriz[1][1] == "O" and matriz[2][1] == "O":
        print("Gana el jugador O")
    elif matriz[0][2] == "O" and matriz[1][2] == "O" and matriz[2][2] == "O":
        print("Gana el jugador O")
    elif matriz[0][0] == "O" and matriz[1][1] == "O" and matriz[2][2] == "O":
        print("Gana el jugador O")
    elif matriz[0][2] == "O" and matriz[1][1] == "O" and matriz[2][0] == "O":
        print("Gana el jugador O")
def ganaJugadorX():
    if matriz[0][0] == "X" and matriz[0][1] == "X" and matriz[0][2] == "X":
        print("Gana el jugador X")
    elif matriz[1][0] == "X" and matriz[1][1] == "X" and matriz[1][2] == "X":
        print("Gana el jugador X")
    elif matriz[2][0] == "X" and matriz[2][1] == "X" and matriz[2][2] == "X":
        print("Gana el jugador X")
    elif matriz[0][0] == "X" and matriz[1][0] == "X" and matriz[2][0] == "X":
        print("Gana el jugador X")
    elif matriz[0][1] == "X" and matriz[1][1] == "X" and matriz[2][1] == "X":
        print("Gana el jugador X")
    elif matriz[0][2] == "X" and matriz[1][2] == "X" and matriz[2][2] == "X":
        print("Gana el jugador X")
    elif matriz[0][0] == "X" and matriz[1][1] == "X" and matriz[2][2] == "X":
        print("Gana el jugador X")
    elif matriz[0][2] == "X" and matriz[1][1] == "X" and matriz[2][0] == "X":
        print("Gana el jugador X")
def menu():
    print("""Las coordenadas que puedes usar son las siguientes:
    1 2 3 
    4 5 6 
    7 8 9""")
while i<3:
    menu()
    jugadorO = int(input("Ingrese la posiscion para marcar la ficha O: ")) #random.randint(1,10)#
    ubicarO(jugadorO)
    imprimirMatriz()
    jugadorX = int(input("Ingrese la posiscion para marcar la ficha X: "))
    ubicarX(jugadorX)
    imprimirMatriz()
    i+=1
ganaJugadorO()
ganaJugadorX()
