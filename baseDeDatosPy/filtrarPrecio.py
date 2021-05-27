import psycopg2

try:
    conn = psycopg2.connect(user="postgres",
                                password="12345",
                                host="127.0.0.1",
                                port="5432",
                                database="Supermercado")
    cursor = conn.cursor()
    #MOSTRAR TODOS LOS REGISTROS DE LA TABLA QUE EL PRECIO SEA MAYOR A 22
    cursor.execute("SELECT * from productos WHERE precio > 22")
    record = cursor.fetchall()
    print("Resultado ", record)
except (Exception, psycopg2.Error) as error:
    print("Error en la conexion...", error)
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Conexion con la base de datos cerrada...")