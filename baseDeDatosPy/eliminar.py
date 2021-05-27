import psycopg2

try:
    conn = psycopg2.connect(user="postgres",
                                password="12345",
                                host="127.0.0.1",
                                port="5432",
                                database="Supermercado")

    cursor = conn.cursor()
    delete_query = """Delete from productos where codigo = 's01'"""
    cursor.execute(delete_query)
    conn.commit()
    count = cursor.rowcount
    print(count, "Registro borrado correctamente...")
except (Exception, psycopg2.Error) as error:
    print("Error al conectar con la base de datos...", error)
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Conexion con la base de datos cerrada...")