import psycopg2

try:
    conn = psycopg2.connect(user="postgres",
                                password="12345",
                                host="127.0.0.1",
                                port="5432",
                                database="Supermercado")

    cursor = conn.cursor()
    # Executing a SQL query to insert data into  table
    sql = """INSERT INTO productos VALUES ('a115','Afilador', 2.50, '2007-11-02');
                        INSERT INTO productos VALUES ('s31','Silla mod. ZAZ', 20, '2007-11-03');
                        INSERT INTO productos VALUES ('s72','Silla mod. XAX', 25, '2007-11-03');"""
    cursor.execute(sql)
    conn.commit()
    print("Registro guardado correctamente...")
except (Exception, psycopg2.Error) as error:
    print("Error en la conexion...", error)
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Conexion con la base de datos cerrada...")