abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
print("Antes ", abecedario)
for x in range(len(abecedario), 1, -1):
    if x % 3 == 0:
        abecedario.pop(x-1)
print("despues", abecedario)