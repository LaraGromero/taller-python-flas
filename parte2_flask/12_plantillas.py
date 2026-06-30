#Plantillas HTML con Jinja2

#Que es Jinja2? es un motor de platillas de Flask, es una de sus gran herramientas. Su función es combinar el codigo python con html para crear paginas dinamicas.

#Carpeta TEMPLATE: Flask predeterminadamente una carpeta llamada templates donde busca los archivos HTML

#Para crear una carpeta templates existen dos formas: 
#La primera es la mas usada que es manualmente, creas la carpeta dentro de tu proyecto visual con 'templates' todo en miniscula
#La segunda manera es abriendo la terminal y escrbiendo 'mkdir templates' en ella.
#La tercera manera es crearla desde un codigo que la crea.

import os #Se importa un modulo en este caso 'os' que permite interactuar con el sistema dejando crear carpetas, renombrar archivos o acceder a rutas.

os.makedirs("templates", exist_ok=True) #Se usa la función makedirs() que crea uno o varias carpetas/directorios.
#exist_ok=True indica que si la carpeta ya existe, que el programa no genere error y continue.

#render_template() en ves de devolver un texto devuelve el archivo HTML
#Como primero se debe importar junto a flask.
from flask import Flask, render_template
#Se debe tener creada ya la carpeta de templates y como minimo un archivo html.

app= Flask(__name__)
@app.route("/") #Se indica la función que respondera cuando se visite esta ruta
def inicio():
    nombre="Laura" #Creamos esta variable con este nombre 
    edad=18 #ejemplo para el {%if%}
    frutas = ["Manzana", "Pera", "Uva"] #ejemplo del {%for%}

    return render_template("index.html", nombre=nombre, edad=edad, frutas=frutas) 
#render_template: Busca el archivo index.html dentro de templates y lo envia al navegador junto a la variable

if __name__=="__main__": # Inicia el servidor. Flask inicua el servidor con app.run()
#Debug=True Es una herramienta para desarrolladores que permite ver errores detallados y recargar automaticamente cuando se guardan cambios.
    app.run(debug=True)
    
#SINTAXIS Jinja2: {{variable}} se utiliza para mostrar el valor de una variables enviada desde flask.
#{% if %} se utiliza para evaluar una condición y mostrar el contenido segun se cumpla la condición o no.
#{%for%} recorre listas, tuplas o diccionarios.
#{% endfor %} finaliza un ciclo for.


