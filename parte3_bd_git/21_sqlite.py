#SQLite con Python — sqlite3
#sqlite3 es el modulo de python que permite crear y administrar bases de datos SQLite
#se importa con: import sqlite 

import sqlite3

conexion = sqlite3.connect("colegio.db") #Se crea la conexión con la base de datos. 
#y si mo exite SQlite lo crea automaticamente

cursor=conexion.cursor()#crea el cursor que es el encargado de ejecutar las consultas SQL

cursor.execute("""
 CREATE TABLE IF NOT EXISTS estudiantes(
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     nombre TEXT NOT NULL,
     edad INTEGER,
     curso INTEGER
 )                  
""") #CREATE TABLE crea una tabla donde se almacenarán los datos.
#IF NOT EXISTS evita que se produzca un error si la tabla ya existe.

#INSERT INTO: se suele utilzar para agregar nuevos registros a la tabla.
#SELECT consulta o recupera la info almacenada.
#commit() guarda permanentemente los cambios realizados en la base de datos.
#close() cierra la conexión con la base de datos.

cursor.execute(
    "INSERT INTO estudiantes(nombre, edad, curso) VALUES(?, ?, ?)",
    ("Julieta", 14, 6) 
) #coloca un nuevo registro en la tabla de estuadiantes

conexion.commit() #Guarda los cambios

resultado= cursor.execute("SELECT * FROM estudiantes").fetchall() #consulta los datos.
print(resultado)

conexion.close() #cierra lo conexión

#Es importantes pq permite guarda la info permanentemente, es utilizado en app pequeñas antes de trabajar con sistemas mas grandes.

