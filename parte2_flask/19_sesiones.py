#Sesiones en Flask — flask.session

#Una sesión permite guardar información de un usuario mientras navega por la aplicación. Ej: nombre de usuario, preferencias o si ha iniciado sesión.
#SECRET_KEY: Es una clave secreta que Flask utiliza para proteger informacion almacenada en la sesióm.
#Es obligatoria si usamos session

#'session' es un diccionario en el cual se pueden guardar datos y leer.
#session["usuario"]= "Laura"  es para guardar.
#usuario = session.get("usuario", "Invitado") si existe usuario devuelve laura, si no devuelve invitado.
#para cerrar 'session' se pueden utilizar dos maneras:
#session.pop("usuario") para eliminar un solo dato.
#session.clear() para eliminar toda la 'session'

from flask import Flask, session, redirect, url_for

app=Flask(__name__)
app.secret_key="Clave_secreta_super" #protege la info de la session

@app.route("/")
def inicio():
    clima=session.get("clima","predeterminado")#Lee uno de los datos
    return f"Hola {clima}"

@app.route("/login")
def login():
    session["clima"]="Lluvioso" #aqui guarda un dato en la session
    return redirect(url_for("inicio"))

@app.route("/logout")
def logout():
    session.pop("clima", None) #elimina un dato de la session y el none es si no existe entonces no hace nada.
    return redirect(url_for("inicio"))

if __name__ == "__main__":
    app.run(debug=True)

#Es importante porque permite recordar la info del usuario entre distintas paginas.