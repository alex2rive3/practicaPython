import psycopg2

try:
    conn = psycopg2.connect(user="postgres",
                                password="12345",
                                host="127.0.0.1",
                                port="5432",
                                database="Supermercado")
    cursor = conn.cursor()
    #MOSTRAMOS TODAS LAS CATEGORIAS SIN QUE SE DUBLIQUE ALGUNA
    cursor.execute("SELECT DISTINCT categoria FROM productos;")
    record = cursor.fetchall()
    print("Resultado ", record)
except (Exception, psycopg2.Error) as error:
    print("Error en la conexion...", error)
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Conexion con la base de datos cerrada...")