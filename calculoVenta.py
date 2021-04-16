print("Bienvenido a su Almacen Favorito")
print("Ingrese los datos de la venta que decea registrar ")
producto = input("Ingrese el nombre del producto ")
precio = float(input("El precio del producto es? "))
cantidad = float(input("Cuanto se ha llevado del producto "))
iva = (precio * cantidad) / 11
subTotal = precio * cantidad - iva
totalAPagar = subTotal + iva
print("El subTotal de la Venta es ", "%.2f" %subTotal , "El iva es del 10% ", "%.2f" %iva)
print("El total a pagar es de ", totalAPagar, "$")