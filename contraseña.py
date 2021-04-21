print("""           Bienvenido!!!!
Necesitamos su contraseña para que pueda ingresar""")
password = "admin1234"
contraseña = str(input("Ingrese su contraseña: ")).lower()
while contraseña != password: 
    print("Contraseña incorrecta, intente nuevamente")
    contraseña = str(input("Ingrese su contraseña nuevamente: ")).lower()
print("Su contraseña fue correcta, ya tiene acceso!!!")