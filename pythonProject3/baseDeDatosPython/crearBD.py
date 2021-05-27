import psycopg2
from psycopg2 import Error
try:
    #establishing the connection
    conn = psycopg2.connect(
        database="postgres", user='postgres', password='12345', host='127.0.0.1', port= '5432'
    )

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    #Preparing query to create a database
    sql = '''CREATE database super'''

    #Creating a database
    cursor.execute(sql)
    conn.commit()
    print("Base de Datos creado Exitosamente........")
except(Exception, Error) as error:  
    print ("Error al Conectar con la base de datos\n", error)
#Closing the connection
finally:
    if conn:
        cursor.close()
        conn.close()
        print("Conexion con PostgreSQL Cerrada")