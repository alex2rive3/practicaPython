import psycopg2

try:
    conn = psycopg2.connect(user="postgres",
                                password="12345",
                                host="127.0.0.1",
                                port="5432",
                                database="Supermercado")

    cursor = conn.cursor()
    #AGREGAMOS LA CATEGORIA A TODOS LOS DATOS DE LA TABLA
    sql = """UPDATE productos SET categoria='utensilio';"""
    cursor.execute(sql)
    conn.commit()
    print("La categoria se agrego correctamente a todos los registros...")
except (Exception, psycopg2.Error) as error:
    print("Error en la conexion...", error)
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Conexion con la base de datos cerrada...")