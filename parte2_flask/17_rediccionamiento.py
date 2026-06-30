#Redireccionamiento y url_for

#Que es redirect(): sirve para enviar al usuario automaticamente a otra ruta
#Ej: cuando se inicia sesión, Flask no te deja en el formulario si no que te manda a otra pagina.

#Que es url_for() Genera la url de una ruta Flask automaticamente.
#Es recomendado para no escribir manualmente las url porque si mañanas cambiamos la ruta en el @app.route tendremos que cambiar el redirect.
# Mientras que con url_for la encuentra solita sin modificar esa linea.

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

if __name__=="__main__":
    app.run(debug=True)
    
# ¿Por qué es importante?
# Después de procesar un formulario es común redirigir al usuario a otra página.
# La url_for() evita escribir las URLs manualmente, haciendo el proyecto más fácil de mantener si las rutas cambian.