import psycopg2
from psycopg2 import Error

try:
    conn = psycopg2.connect(user="postgres",
                                password="12345",
                                host="127.0.0.1",
                                port="5432",
                                database="Supermercado")
    cursor = conn.cursor()
    #SQL PARA CREAR UNA TABLA EN LA BASE DE DATOS 
    sql = '''CREATE TABLE productos (
                                    codigo VARCHAR(5),
                                    nombre VARCHAR(30),
                                    precio INT,
                                    fechaAlta DATE,
                                    PRIMARY KEY (codigo)); '''
    # Execute a command: this creates a new table
    cursor.execute(sql)
    conn.commit()
    print("Tabla creada exitosamente....")

except (Exception, Error) as error:
    print("Error al conectar con la base de datos PostgreSQL", error)
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Conexion a la Base de Dato cerrada")
