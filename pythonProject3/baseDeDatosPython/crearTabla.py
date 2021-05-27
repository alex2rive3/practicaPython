import psycopg2
from psycopg2 import Error

try:
    conn = psycopg2.connect(user="postgres",
                                password="12345",
                                host="127.0.0.1",
                                port="5432",
                                database="consultasHospital")

    cursor = conn.cursor()
    # SQL query to create a new table
    sql = '''CREATE TABLE consultas
            (ID INT PRIMARY KEY     NOT NULL,
            paciente        TEXT    NOT NULL,
            doctor          TEXT,
            fecha           TEXT,
            motivo          TEXT); '''
    # Execute a command: this creates a new table
    cursor.execute(sql)
    conn.commit()
    print("Table created successfully in PostgreSQL ")

except (Exception, Error) as error:
    print("Error al conectar con la base de datos PostgreSQL", error)
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Conexion con Postgrest cerrada")
