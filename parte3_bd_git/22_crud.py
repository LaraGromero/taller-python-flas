# Integración Flask + SQLite — CRUD básico

# Flask puede conectarse a una base de datos SQLite para guardar y consultar información.
# CRUD son las cuatro operaciones básicas que se realizan en una base de datos:
# C(Create): Crear o insertar nuevos registros.
# R(Read): Leer o consultar los registros.
# U(Update): Actualizar o modificar un registro.
# D(Delete): Eliminar un registro.

#Flask abre una conexion a la bd cada vez que le llega una solicitud del usuario y la cierra cuando la operación termina. Evita dejar conexiones abiertas y mejora el rendimiento

from flask import Flask, render_template, request
import sqlite3

app=Flask(__name__)

#PARA LEER:
@app.route("/")
def lista():
    conexion=sqlite3.connect("colegio.db")
    cursor=conexion.cursor()
    
    estudiantes= cursor.execute("SELECT * FROM estudiantes").fetchall()
    conexion.close()
    return render_template("estudiantes.html", estudiantes=estudiantes)

#PARA CREAR:
@app.route("/agregar", methods=["POST"])
def agregar():
    nombre=request.form["nombre"]
    edad=request.form["edad"]
    curso=request.form["curso"]
    
    conexion=sqlite3.connect("colegio.db")
    conexion.execute(
        "INSERT INTO estudiantes(nombre, edad, curso) VALUES (?, ?, ?)",
        (nombre, edad, curso)
    ) #coloca un nuevo registro en la tabla de estuadiantes
    
    conexion.commit() #Guarda los cambios
    conexion.close() #Cierra la conexion.
    
    return "Has registrado al estudiante exitosamente"

if __name__=="__main__":
    app.run(debug=True)
    
#Es importante porque permite guardar la info enviada desde los formularios y consultarla posteriormente.
#Es comun que se utilice en proyectos pequeños o medianos, ya que facilita el desarrollo de la web con base de datos.