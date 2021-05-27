import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                    password="12345",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="consultasHospital")
    cursor = connection.cursor()
    print("Conexion establecida correctamente...")

except (Exception, psycopg2.Error) as error:
    print("Error en la conexion con la base de datos", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Conexion a PostgreSQL cerrada")