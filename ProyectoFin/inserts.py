import psycopg2
from psycopg2 import DatabaseError

def conexion():
    try:
        return psycopg2.connect(
            host='localhost',
            user='postgres',
            password='admin',
            database='proyectoIATraductores',
            port = '5432'
        )
    except DatabaseError as ex:
        raise ex
    
database = conexion()
id_participante = 6
id_juego = 6
n1 = 25
n2 = 5
n3 = 5
n4 = 25
n5 = 40
seleccion1 = "C"
seleccion2 = "D"
seleccion3 = "C"
seleccion4 = "D"
seleccion5 = "A"

cursor = database.cursor()
j = 0
for i in range(n1):
    j+=1
    print(i)
    cursor.execute('INSERT INTO resultado (id_juego, id_participante, iteracion, seleccion) VALUES (%s, %s, %s, %s)', (id_juego, id_participante, j, seleccion1))
    database.commit()

for i in range(n2):
    j+=1
    print(i)
    cursor.execute('INSERT INTO resultado (id_juego, id_participante, iteracion, seleccion) VALUES (%s, %s, %s, %s)', (id_juego, id_participante, j, seleccion2))
    database.commit()

for i in range(n3):
    j+=1
    print(i)
    cursor.execute('INSERT INTO resultado (id_juego, id_participante, iteracion, seleccion) VALUES (%s, %s, %s, %s)', (id_juego, id_participante, j, seleccion3))
    database.commit()

for i in range(n4):
    j+=1
    print(i)
    cursor.execute('INSERT INTO resultado (id_juego, id_participante, iteracion, seleccion) VALUES (%s, %s, %s, %s)', (id_juego, id_participante, j, seleccion4))
    database.commit()

for i in range(n5):
    j+=1
    print(i)
    cursor.execute('INSERT INTO resultado (id_juego, id_participante, iteracion, seleccion) VALUES (%s, %s, %s, %s)', (id_juego, id_participante, j, seleccion5))
    database.commit()

#70