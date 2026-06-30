#Manejo de errores — 404 y 500

#Que es @app.errorhandler? es un decorador que permite manejar errores especificos.

#ERROR 404: "pagina no encontrada", sucede cuando se ejecuta una dirección que no existe.
#ERROR 500: "Error interno del servidor", sucede cuando el programa falla por un error inesperado mientras procesa la solicitud
#En vez de mostrar estos tipicos errores podemos mostrar paginas mas personalizadas.

from flask import Flask, redirect, url_for, render_template

app=Flask(__name__)

@app.route("/")
def inicio():
    return render_template("form.html")

@app.route("/pagina")
def pagina():
    return render_template("pagina.html")

@app.route("/guardar", methods=["POST"])
def guardar():
    return redirect(url_for("pagina")) 
# redirect() redirige al usuario a otra ruta, en este caso a pagina.
# url_for() busca la ruta asociada a la función "pagina" y genera la URL automáticamente.

@app.errorhandler(404)
def noencontrada(error):
    return render_template("404.html"), 404 #muestra nuestra pagina personalizada, y el 404 indica que el codigo de respuesta sigue siendo ese

@app.errorhandler(500)
def errorservidor(error):
    return render_template("500.html"), 500 # Muestra la página personalizada y mantiene el código de respuesta HTTP 500.

if __name__=="__main__":
    app.run(debug=True)
    
#Es importante porque le da mas identidad a nuestra pagina y mejora la experiencia del usuario tambien hace que se vea mas profesional