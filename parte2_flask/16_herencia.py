#Herencia de plantillas — base.html y block
# ¿Que es base.html? Es la plantilla que tiene las partes comunes de las paginas como el header, el navbar, footer o enlaces al css.

#{%extends %}: permite que una pagina utilice el contenido de base.html
# {% block %}: sección que puede ser reemplazada por las paginasa que utilicen a base.html. Espacio para que otra página escriba ahi su contenido.  
#{% block contenido %}: Es el bloque donde irá el contenido específico de cada página.

from flask import Flask, render_template

app=Flask(__name__)
@app.route("/")
def inicio():
    return render_template("pagina.html")

if __name__=="__main__":
    app.run(debug=True)

