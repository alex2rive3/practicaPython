curso = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
creditos = 0
for key in curso:
    print(key, " tiene ", curso[key], "creditos")
    creditos += curso[key]
print("Numero total de creditos en el curso: ", creditos)