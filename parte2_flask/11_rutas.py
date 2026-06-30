#Rutas y Decoradores — @app.route

from flask import Flask, request
app= Flask(__name__)

# cómo funciona el decorador @app.route
@app.route("/catalogo")
#@ funciona para agregar comportamientos a la función de abajo. Indica un decorador.
#app.route() Metodo de Flask que sirve para indicar una ruta y que luego se ejecute una función, dentro de los parentesis colocaremos la ruta.
def menu():
    return "Mira nuestros productos!"

#Multiples rutas, los aplicativos utilizan muchas porque cada ruta representa una parte de la pagina diferente, inicio, catalogo, sobre nosotros.
#o para manejar varias rutas, ya sea para leer, escribir, mover o procesar datos en diferentes ubicaciones. Es comun cuando:
#necesitamos procesar archivos en varias carpetas, tener rutas dinamicas dependiendo del sistema opertario, trabajar con rutas relativas y absolutas al mismo tiempo.
#Ruta absoluta: C:/Users/Usuario/documento.txt (Windows) Ruta relativa: ./datos/archivo.csv (relativa al script actual).


#RUTAS CON VARIABLES: permiten recibir datos/parametros en las rutas y trabajar con ellos.

@app.route("/ubicación/<ciudad>") #aqui <ciudad> es una variable, cuando el usuario ejecute va a tomar el ultimo valor de la URL
def ubicación(ciudad): 
    return f"Estas ubicado en: {ciudad}"

#GET y POST métodos HTTP usados para comunicarse con servidores Web, pero con claras diferencias por los menos GET Obtiene/solicita datos del servidor, se envian por clave=valor y es ideal para consultas.
#Mientras que post envia datos al servidor por ejemplo inicio de sesión, enviar formularios. Es mas seguro y dejas enviar mas información.

@app.route("/formulario", methods=["GET"]) #Para utlizarlo debemos separar la ruta con una , y colocar el metodo
def formulario(): 
    return f"formulario de registro"

@app.route("/registro", methods=["POST"])
def registro():
    return "Usuario registrado."

if __name__=="__main__": # Inicia el servidor. Flask inicua el servidor con app.run()
#Debug=True Es una herramienta para desarrolladores que permite ver errores detallados y recargar automaticamente cuando se guardan cambios.
    app.run(debug=True)

