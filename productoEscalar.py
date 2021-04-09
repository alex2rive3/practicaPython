vector1 = [1,2,3]
vector2 = [-1,0,2]
resultado = 0
for x in range(0,len(vector1)):
    resultado= resultado+(vector1[x]*vector2[x])
print("el producto escalar de ambos vectores es ", resultado)