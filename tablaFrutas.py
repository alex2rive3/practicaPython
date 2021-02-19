frutas = {"Plátano": 1.35,
"Manzana": 0.80,
"Pera": 0.85,
"Naranja": 0.70}
fruta = input("Que fruta decea comprar? ").title()
kilos = int(input("Cuantos kilos? "))
if fruta in frutas:
    print(kilos, 'kilos de', fruta, 'valen', frutas[fruta]*kilos, "$")
else: 
    print("Lo siento, la fruta", fruta, "no está disponible.")