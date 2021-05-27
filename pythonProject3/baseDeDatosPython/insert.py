import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                password="12345",
                                host="127.0.0.1",
                                port="5432",
                                database="consultasHospital")

    cursor = connection.cursor()
    # Executing a SQL query to insert data into  table
    insert_query = """INSERT INTO consultas (id,paciente,doctor,fecha,motivo)
	VALUES (3,'paciente15','doctor1','20/03/2021','Consulta preventiva');"""
    cursor.execute(insert_query)
    connection.commit()
    print("El nuevo registro se pudo guardar correctamente...")
    # Fetch result
    cursor.execute("SELECT * from consultas")
    record = cursor.fetchall()
    print("Result ", record)
except (Exception, psycopg2.Error) as error:
    print("Error en la conexion...", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Conexion con la base de datos cerrada...")