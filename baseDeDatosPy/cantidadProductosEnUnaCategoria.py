import psycopg2

try:
    conn = psycopg2.connect(user="postgres",
                                password="12345",
                                host="127.0.0.1",
                                port="5432",
                                database="Supermercado")
    cursor = conn.cursor()
    #MOSTRAR LA CANTIDAD DE PRODUCTOS EXISTETNTES EN CADA CATEGORIA
    cursor.execute("SELECT categoria, count(*) FROM productos GROUP BY categoria;")
    record = cursor.fetchall()
    print("Resultado ", record)
except (Exception, psycopg2.Error) as error:
    print("Error en la conexion...", error)
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Conexion con la base de datos cerrada...")