n = int(input("Introduce la altura del triángulo (entero positivo): "))
for x in range(1, n+1, 2):
    for i in range(x, 0, -2):
        print(i, end=" ")
    print("")
input("")