import psycopg2

try:
    conn = psycopg2.connect(user="postgres",
                                password="12345",
                                host="127.0.0.1",
                                port="5432",
                                database="Supermercado")

    cursor = conn.cursor()
    #AGREGAMOS LA CATEGORIA SILLA A TODOS CUYOS NOMBRES SEAN SILLA
    sql = """UPDATE productos SET categoria='silla' WHERE LEFT(nombre,5) = 'Silla';"""
    cursor.execute(sql)
    conn.commit()
    print("La categoria sea moficado coreectamente todos los registros Seleccionados...")
except (Exception, psycopg2.Error) as error:
    print("Error en la conexion...", error)
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Conexion con la base de datos cerrada...")