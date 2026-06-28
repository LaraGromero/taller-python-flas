#Primera aplicacion Flask — app.py y servidor de desarroll
from flask import Flask 
#App.py es el archivo principal de la aplicación.

#Para crear el objeto app. esta linea crea el objeto principal de la aplicación.
app= Flask(__name__) #app es el objeto principal y Flask es una clase de la libreria que crea la app web
#__name__ variable que indica el nombre del archivo que se está ejecutando y ayuda a Flask a localizar recursos del proyecto.


@app.route("/") #La ruta es una dirección que el usuario visita en el navegador. Aqui se define la ruta raiz.
#@ funciona para agregar comportamientos a la función de abajo. Indica un decorador.
#app.route() Metodo de Flask que sirve para indicar una ruta y que luego se ejecute una función.
#/ suele representar la ruta raiz o el inicio de la pagina.

def inicio():  #Función que se ejecuta cuando entran a esa ruta
    return "Bienvenido a pizzeria la 32" #Esto es lo que vera el usuario en el navegador porque Flask lo envia al navegador

if __name__ == "__main__": #Cuando el archivo se ejecuta directamente su valor es __main__
#esta linea verifica si el archivo se ejecuta directamente, lo hace solo en ese caso. Si es importado no.
    app.run(debug=True) ## Inicia el servidor. Flask inicua el servidor con app.run()
#Debug=True Es una herramienta para desarrolladores que permite ver errores detallados y recargar automaticamente cuando se guardan cambios.