# Formularios HTML y metodo POST
#Un formulario HTML con metodo post se utiliza para enviar info al servidor. Es comun para enviar contraseñas o formularios de registro.
#Primero se debe crear el archivo html y crear un formulario.

from flask import Flask, render_template, request
app=Flask(__name__)

@app.route("/")
def inicio():
    return render_template("form.html")
    

@app.route("/guardar", methods=["POST"]) #Utilizamos el metodo POST Porque enviamos datos al servidor, y que se ejecutara cuando entremos en /guardar
def guardar(): 
    if request.method== "POST":  #request contiene toda la info que envio el navegador y method dice que metodo se utilizo es este caso post
        nombre=request.form["nombre"]  #request.form contiene los datos enviados por el formulario y el 'nombre' tiene que ser exacto al atributo de name= en HTML
        apellido=request.form["apellido"]
        preferencia=request.form["preferencia"]
        return f"hola! tus datos son: {nombre} {apellido} y tu color fav es: {preferencia}"

if __name__=="__main__":
    app.run(debug=True)
    
    
#GET y POST métodos HTTP usados para comunicarse con servidores Web, pero con claras diferencias por los menos GET Obtiene/solicita datos del servidor, se envian por clave=valor y es ideal para consultas.
#Mientras que post envia datos al servidor por ejemplo inicio de sesión, enviar formularios. Es mas seguro y dejas enviar mas información.
#request.form permite acceder a los datos enviados desde un formulario HTML mediante el método POST.



