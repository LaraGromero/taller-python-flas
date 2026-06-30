#Variables de URL y parametros de consulta
from flask import Flask, request
app= Flask(__name__)
#RUTAS CON VARIABLES: permiten recibir datos/parametros en las rutas y trabajar con ellos. Se llamas rutas variables porque una parte es fija(ruta) y la otra variable

#TIPOS DE CONVERSORES: por defecto todo lo que llega de la URL es un string.
#Flask permite indicar el tipo de dato que esperas con lo siguiente:
#@app.route("/usuario/<string:nombre>")  si es texto
#<int:id>" para dato numerico
#<float:valor> para dato decimal. y si no recibe el tipo de dato que espera genera un error 404

@app.route("/")
def inicio():
    return "Bienvenido"

@app.route("/ubicación/<string:ciudad>") #aqui <ciudad> es una variable, cuando el usuario ejecute va a tomar el ultimo valor de la URL y esperara un dato string
def ubicación(ciudad): 
    return f"Estas ubicado en: {ciudad}"

#Parámetros de consulta  con request.args:se utiliza para acceder a los parametos enviados en la URL por medio de GET
#son diferentes a las rutas con variables porque en vez de escribir: /ubicación/<ciudad>, se escribe /buscar?ciudad=palmira (es un ejemplo) como parametos de consulta.

#request.args.get("ciudad","") busca el parametro ciudad, si no existe, devuelve una cadena vacia como valor predeterminado

@app.route("/buscar")
def buscar():
    ciudad=request.args.get("ciudad", "")
    return f"buscar la ciudad: {ciudad}"

if __name__=="__main__":
    app.run(debug=True)
    
#Son importantes proque son muy utilizados en APIs Rest y en Paginas web para mostar info dinamica  y responder a las solicitudes de los usuarios.