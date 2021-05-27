import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                    password="12345",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="consultasHospital")

    cursor = connection.cursor()

    update_query = """Update consultas set fecha = '23/05/2021',motivo = 'Gripe sebera' where id = 1"""
    cursor.execute(update_query)
    connection.commit()
    #count = cursor.rowcount
    print("La modificacion se realizo excitosamente...")


except (Exception, psycopg2.Error) as error:
    print("Error al conectar con la base de datos...", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Conexion a la base de datos cerrada...")