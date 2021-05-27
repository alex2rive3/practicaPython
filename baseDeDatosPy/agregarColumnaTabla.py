import psycopg2

try:
    conn = psycopg2.connect(user="postgres",
                                password="12345",
                                host="127.0.0.1",
                                port="5432",
                                database="Supermercado")

    cursor = conn.cursor()
    #AGREGAMOS UNA COLUMNA LLAMADA CATEGORIAS A LA TABLA PRODUCTOS
    sql = """ALTER TABLE productos ADD categoria varchar(10);"""
    cursor.execute(sql)
    conn.commit()
    print("La columna se agrego correctamente...")
except (Exception, psycopg2.Error) as error:
    print("Error en la conexion...", error)
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Conexion con la base de datos cerrada...")