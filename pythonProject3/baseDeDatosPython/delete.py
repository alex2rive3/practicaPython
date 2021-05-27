import psycopg2

try:
    conn = psycopg2.connect(user="postgres",
                                password="12345",
                                host="127.0.0.1",
                                port="5432",
                                database="consultasHospital")

    cursor = conn.cursor()
    delete_query = """Delete from consultas where id = 1"""
    cursor.execute(delete_query)
    conn.commit()
    count = cursor.rowcount
    print(count, "Registro borrado correctamente...")
    # Fetch result
    cursor.execute("SELECT * from consultas")
    print("Result ", cursor.fetchall())


except (Exception, psycopg2.Error) as error:
    print("Error al conectar con la base de datos...", error)
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Conexion con la base de datos cerrada...")