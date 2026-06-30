from flask import Flask, render_template, request, jsonify, session, url_for, redirect
import sqlite3
app=Flask(__name__)
conexion= sqlite3.connect("agenda.db")
cursor=conexion.cursor()

cursor.execute("""
 CREATE TABLE IF NOT EXISTS contactos(
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     nombre TEXT NOT NULL,
     telefono TEXT NOT NULL,
     correo TEXT NOT NULL
 )                  
""") #Utilizo text en telefono porque algunos numeros reales pueden empezar por el prefijo o tener guiones o espacios.



conexion.commit()
conexion.close()

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/contactos")
def mostrar():
    conexion= sqlite3.connect("agenda.db")
    cursor=conexion.cursor()
    contactos= cursor.execute("SELECT * FROM contactos").fetchall() #consulta los datos.
    conexion.close()
    return render_template("contactos.html", contactos=contactos)

@app.route("/agregar", methods=["POST"])
def agregar(): 
    nombre=request.form["nombre"]  
    telefono=request.form["telefono"]
    correo=request.form["correo"]
        
    conexion=sqlite3.connect("agenda.db")
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO contactos(nombre, telefono, correo) VALUES (?, ?, ?)",
        (nombre, telefono, correo))
    
    conexion.commit() #Guarda los cambios
    conexion.close() #Cierra la conexion.
    
    return redirect(url_for("mostrar"))

@app.route("/agregarop")
def agregarop():
    return render_template("formulario.html")

@app.route("/eliminar/<int:id>")
def eliminar(id):
    conexion= sqlite3.connect("agenda.db")
    cursor=conexion.cursor()
    cursor.execute(
        "DELETE FROM contactos WHERE id= ?", (id,)
    )
    conexion.commit()
    conexion.close()
    return redirect(url_for("mostrar"))

@app.route("/buscar", methods=["GET"])
def buscar():
    nombre=request.args.get("nombre", "")
    busqueda = f"%{nombre}%"
    
    conexion= sqlite3.connect("agenda.db")
    cursor=conexion.cursor() 
    
    contactos=cursor.execute(
        "SELECT * FROM contactos WHERE nombre LIKE ?",(busqueda,)
        ).fetchall()
    conexion.close() 
    return render_template("contactos.html", contactos=contactos)
    
if __name__ == "__main__":
    app.run(debug=True)
    
