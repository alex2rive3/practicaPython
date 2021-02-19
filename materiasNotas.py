materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
for x in materias:
    print("cual fue tu nota en ", x)
    nota=input()
    notas.append(nota)
for i in range(len(materias)):
    print("En ", materias[i], "has quitado una nota de ", notas[i])
input()