#API REST con Flask — respuestas JSON

#Que es uan ApiRest? permite que diferentes apps se comuniquen entre si mediante solicitudes http (get, post, put, delete)
#Json es un formato para intercambiar datos, es facil de leer para personas y programas.
#jsonify() convierte listas o diccionarios de python a formato Json para enviarlos.

# para utlizarlo se tiene que importar jsonify y se puede utilizar para mensajes:
#return jsonify({"mensaje": "Hola Mundo"}) 
#o para enviar varias variables o listas,o lista de diccionarios:
# def usuario():
#   nombre = "Laura"
#    edad = 16
#    ciudad = "Cali"
#    return jsonify({
#        "nombre": nombre,
#        "edad": edad,
#        "ciudad": ciudad  })


#ENDPOINT: es una ruta de la API por la cual se recibe o devuelve información. En mi ejemplo deevuelven datos en formato json.


from flask import Flask, jsonify

app=Flask(__name__)

@app.route("/")
def inicio():
    return "Bienvenido a la API"

@app.route("/api/direcciones") #Estos son los endpoints
def direccion():
    direc=[{
        "id":1,
        "ciudad":"Palmira",
        "direccion":"Calle 42 #15-20",
    },
    {
        "id":2,
        "ciudad":"Cali",
        "direccion":"Carrera 42 #30-12"
    }]
    
    return jsonify(direc)

@app.route("/api/empresa") #Estos son los endpoints
def empresa():
    return jsonify({
        "nombre":"Ferreteria Villa",
        "estado":"Abierto"
    })
    
if __name__=="__main__":
    app.run(debug=True)
    
    
#Como probar la API? Se escribe en la ruta de navegación http://127.0.0.1:5000/api/direcciones o http://127.0.0.1:5000/api/empresa
#o se puede utilizar postman para enviar solicitudes http y ver las respuestas en formatos JSON.