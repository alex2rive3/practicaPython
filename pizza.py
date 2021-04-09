eleccion = int(input("Precione 1 si decea una pizza vegetaria \nPreciones 2 para una pizza no vegetariana "))
if eleccion==1:
    eleccion="vegetriana"
    ingrediente = str(input("Elija uno de los siguientes ingredientes: Pimiento o tofu. "))
elif eleccion==2:
    eleccion= "no vegetariana"
    ingrediente = str(input("Elija uno de los siguientes ingredientes: Peperoni, Jamón y Salmón. "))
print("el tipo de pizza seleccionado fue ", eleccion, " y los ingredientes de la misma son  mozzarella, tomate  y ", ingrediente)
input()