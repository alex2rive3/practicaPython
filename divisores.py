numero = 20 
lista =[]
i=numero
while i > 1:
    if numero%i == 0:
        print (i)
        lista.append(i)
    i-=1
print(lista)
input()
