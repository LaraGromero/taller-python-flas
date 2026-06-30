# Investigación: Taller Python y Flask

# PUNTO 1 ********************************************

# ¿Que es una variable? Una variable es basicamente una caja donde se puede guardar información y esta utiliza una etiqueta para poder identificarla. 

# Las variables pueden almacenar diferentes tipos de datos, como números, texto, booleanos, entre otros. Estos suelen ser los mas comunes.

# edad= 25 En este caso la etiqueta es 'edad' y el valor que tiene es 25, y es valor tipo de dato entero (int).

# print (type(edad))  Esto nos permite ver el tipo de dato que tiene la variable 'edad' en este caso es int.
# fruta= "Manzana" 
# En este caso la etiqueta es 'fruta' y el valor que tiene es "Manzana", y es valor tipo de dato cadena de texto (str).

# nota= 3.4 
# En este caso la etiqueta es 'nota' y el valor que tiene es 3.4, y es valor tipo de dato decimal (float)

# activo= True 
# En este caso la etiqueta es 'activo' y el valor que tiene es True, y es valor tipo de dato booleano (bool).


# ¿Que es tipado dinamico? Python brinda una flexibilidad al permitir que una variables pueda cambiar de tipo durante el programa, donde puede empezar siendo un tipo de dato (str) y luego podemos cambiarlo a dato entero.

# PUNTO 2 ********************************************

# If se utiliza para ejecutar un bloque de código si una condición es verdadera. Un ejemplo en la vida cotidiana seria:
# Quiero comprar un helado, pero solo si tengo dinero. ¿Tengo dinero? Si, compro el helado. ¿Tengo dinero? No, no compro el helado.

# Else se utiliza para ejecutar si la condición no cumple con if ni con elif.
    
# Elif se utiliza para agregar condiciones adicionales a un bloque if. Un ejemplo en la vida cotidiana seria: 
# Para sacar un exelente en un examen debo sacar mayor o igual a 4.5, para sacar regular debo sacar mayor o igual a 3.5, y para sacar insuficiente debo sacar menor a 3.5.

# Para la identación es muy importante que despues de cada if, elif y else se deben colocar ':' y 4 espacios para seguir escribiendo el codigo correspondiente a cada bloque.

# Ademas todos los if, elif y else deben estar alineados al mismo nivel. Ejemplo de mal:


# if tengo_dinero == True: 
# print("Compro el helado") #Aqui da error y debe estar alineado con los 4 espacios de identación.
# else: #Si no se colocan los ':' al final de cada if, elif y else, tambien dara error porque ese es el simbolo que indica el inicio de un bloque de código.
#     print("No compro el helado")

# COMPARACIÓN DE VALORES: Para ejecutar un bloque de código si una condición es verdadera, se utilizan operadores de comparación. Los operadores de comparación son los siguientes:
# ==   igual que
# !=   diferente de
# >    mayor que
# <    menor que
# >=   mayor o igual
# <=   menor o igual

# INCLUYO LOS CONECTORES LOGICOS: Para combinar varias condiciones, se utilizan operadores lógicos. Los operadores lógicos son los siguientes:
# and  y
# or   o

# PUNTO 3 ********************************************

# Que son los ciclos?
# Los ciclos son estructuras de control que permiten repetir un bloque de código varias veces.
# La repetición puede depender de una condición (while) o de una colección de elementos (for). Ademas ayudan a reducir la repetición de codigo haciendo los programas mas cortos y faciles.

# DIFERENCIA ENTRE FOR Y WHILE
# FOR: Se utiliza cuando necesito recorrer cada elemento de una lista, tupla o cadena de texto, porque ya conozco los elementos que voy a recorrer.

# WHILE: cuando necesito repetir una acción hasta que se cumpla una condición determinada. 
# Por ejemplo, un contador, una calculadora, un menú o la solicitud de datos al usuario hasta que ingrese una respuesta válida.

# Break: se utiliza para salir de un ciclo cuando se cumple una condición determinada. Detiene completamente el ciclo.

# Continue: se utiliza para saltar a la siguiente iteración del ciclo cuando se cumple una condición determinada. 

# PUNTO 4 ********************************************

# ¿Que son las funciones? Son bloques de codigo que realizan una tarea específica, reducen la repetición de codigo. Son como un bloque con instrucciones que se peude reutilizar.

# Como se define una función? Se define con la palabra reservada 'def' seguida del nombre de la función y paréntesis. 

# Que es un parámetro? Es una variable que se define dentro de la función y recibe unos valores especificos.
# Valores por defecto son los cuales se asignan a los parametros en caso de que el usuario no ingrese un valor.
# Return entrega un valor para seguir trabajando con él. Mientras que print muestra el valor en la pantalla. 

# PUNTO 5 ********************************************
# LISTA: Se crea nombrando una variable y encerrando los elementos entre []. Es uno de los tipos de datos mas utilizados porque sus datos los podemos cambiar.
# lista= ["rojo","verde","azul"]
# Para acceder a ellas necesitamos tener en cuenta las posiciones donde "rojo" es nuestro primer elemento pero tiene la posición 0.
# print (lista[1])
# para modificar tambien usaremos lo de las posiciones, llamarelos la lista y la posición y le asignamos un nuevo valor.
# lista[0]= "rosado"
# print (lista)
# para agregar nuevos elementos a una lista se usa .append que solo puede agregar de un elemento.
# lista.append("rojo") se coloca el valor nuevo entre ()
# para recorrer usariamos for. for color in lista: print(color)

# TUPLAS: Son parecidas a la listas pero no se pueden cambiar sus valores sirven para valores especificos como fechas de nacimientos, registros de pagos, etc.
# Utiliza parentesis en vez de corchetes.
# Tambien para acceder a ellas se usa posiciones.
# Tambien se puede usar for para recorrerla.

# DICCIONARIO permite almacenar una clave con un dato. Las claves deben ser unicas, inmutables y tipo string y entero. Se puede agregar diccionarios, listas, cadenas y se define {}
# es necesario que esten separadas por : porque indica el valor de la clave y separadas por una , para saber donde termina la clave
# Para acceder llamamos el diccionario y entre [] escribimos la clave.
# PARA MODIFICAR
# factura["nombre"]= "Santiago"
# PARA AGREGAR
# factura["ciudad"]= "Palmira"
# Para recorrer tenemos que usar for que vuelve 

# for clave in factura:
#    print (clave)
    
# for valor in factura.values():
#    print (valor)
    
# for clave, valor in factura.items(): 
# Agarra cada par del diccionario y los separa.
#    print(clave, valor) 
# Es lo mas usado para recorrer claves y valores al mismo tiempo
# PUNTO 6 ********************************************
# OPEN() basicamente es como abrir el archivo para poder trabajar con el.
    
# 'r' (read) modo de apertura, el cual hace que lea el archivo no lo modifica.
# 'w' (write)  escribe pero si el archivo ya tenia contenido, borra y escribe de nuevo.
# 'a' (append) agrega información al final del documento.

# Metodos.
# with permite que el archivo se cierre automaticamente al terminar. 
# write() permite escribir dentro de un archivo que ya fue abierto.
# para leer linea por linea se suele usar for.
# strip() en el taller aparece como ejemplo, su proposito es quitar espacios y saltos de linea sobrantes.



# PUNTO 7 ********************************************
# Resuelve problemas que hagan que el programa se detenga y genere error. Evita que el programa se detenga por errores y permite dar mensajes claros o tomar acciones correctivas.

#  TRY: aqui se suele colcar codigos que podrian fallar
# EXCEPT: Se ejecuta si ocurre un error para corregirlo y evitar que el programa se detenga. Captura errores
# ValueError es una de las excepciones especificas y un ejemplo claro es cuando un usuaria digita un tipo de dato incorrecto, "hola" donde debia ir un dato numerico.
# ZeroDivisionError existe para evitar o ignorar las divisiones por 0
# finally: Su proposito es ejecutar un codigo haya error o no. Su uso típico es para liberar recursos o cerrar conexiones que se hayan abierto en Try.
# IndexError: Sucede cuando piden una posición que no existe
# Ejemplo sobre como iria su estructura en la vida real: 
# Try: Intentar abrir una puerta, pero esta cerrada.
# Except: Usar otra puerta.
# finally: Cerrar la puerta.
# PUNTO 8 ********************************************
# Forma de estructura de programas el cual se centra en programar objetos o entidades del mundo real.
# Basicamente: Un objeto tiene caracteristicas y comportamientos. 
# Clase es como un molde para crear muchas instancias
# class es reservada para crear clase, primero se llama y luego se nombra con lo eligamos.
# es el constructor de la clase, ejecuta automáticamente cuando se crea un objeto y sirva para definir los atributos
# Self hace referencia al objeto/instancia. Son las características o datos que pertenecen a cada objeto creado a partir de la clase.
# Son funciones definidas dentro de una clase que permiten realizar acciones o trabajar con los atributos del objeto.
# print (animal1.metodo()) Esta manera de mostrar los datos con print aparece None porque hace print a una función que no devuelve nada. 
# animal1.metodo() Manera correcta

# PUNTO 9 ********************************************
# Que es Flask y como instalarlo
# ¿QUE ES UN FRAMEWORK? En pocas palabras son las herramientas y estructuras ya hechas para el desarrollo de aplicativos.
# Ej cotidiano: al construir una casa necesitamos planos, herramientas eso es un framework.
# ¿QUE ES UN MICROFRAMEWORK? Como lo dice la palabra MICRO trae cosas mas sencillas y esenciales de un framework normal. 
# Flask es considerado un MICROframework porque es flexible, sencillo, tiene pocas herramientas integradas.
# DIFERENCIAS CON DJANGO
# Django es un framework desde ahi esta la diferencias porque al ser un framework esta mas completo, tiene mas herramientas, es mas pesado, recomendado para proyectos grandes.
# Como instalar Flask
# En tu terminal escribres
# pip install flask 
# Pip es el gestor de paquetes de Python, lo solemos utilizar para instalar librerias.

# Para verificar tenemos dos maneras totalmente validas que nos dan el mismo resultado.
# import flask; 
# print(flask.__version__) #3.1.2 dice esto en la terminal

# python -c "import flask; print(flask.__version__)" escribir esto en tu terminal que arroja a lo mismo

# PUNTO 10 ********************************************

#  Primera aplicacion Flask — app.py y servidor de desarroll
# from flask import Flask 
# App.py es el archivo principal de la aplicación.

# Para crear el objeto app. esta linea crea el objeto principal de la aplicación.
# app= Flask(__name__) app es el objeto principal y Flask es una clase de la libreria que crea la app web
# __name__ variable que indica el nombre del archivo que se está ejecutando y ayuda a Flask a localizar recursos del proyecto.

# La ruta es una dirección que el usuario visita en el navegador. Aqui se define la ruta raiz.
# @ funciona para agregar comportamientos a la función de abajo. Indica un decorador.
# app.route() Metodo de Flask que sirve para indicar una ruta y que luego se ejecute una función.
# / suele representar la ruta raiz o el inicio de la pagina.
# Cuando el archivo se ejecuta directamente su valor es __main__
# esta linea verifica si el archivo se ejecuta directamente, lo hace solo en ese caso. Si es importado no.
#    app.run(debug=True) # Inicia el servidor. Flask inicua el servidor con app.run()
# Debug=True Es una herramienta para desarrolladores que permite ver errores detallados y recargar automaticamente cuando se guardan cambios.

# PUNTO 11 ********************************************
# cómo funciona el decorador @app.route

# @ funciona para agregar comportamientos a la función de abajo. Indica un decorador.
# app.route() Metodo de Flask que sirve para indicar una ruta y que luego se ejecute una función, dentro de los parentesis colocaremos la ruta.

# Multiples rutas, los aplicativos utilizan muchas porque cada ruta representa una parte de la pagina diferente, inicio, catalogo, sobre nosotros.
# o para manejar varias rutas, ya sea para leer, escribir, mover o procesar datos en diferentes ubicaciones. Es comun cuando:
# necesitamos procesar archivos en varias carpetas, tener rutas dinamicas dependiendo del sistema opertario, trabajar con rutas relativas y absolutas al mismo tiempo.
# Ruta absoluta: C:/Users/Usuario/documento.txt (Windows) Ruta relativa: ./datos/archivo.csv (relativa al script actual).


# RUTAS CON VARIABLES: permiten recibir datos/parametros en las rutas y trabajar con ellos.

# GET y POST métodos HTTP usados para comunicarse con servidores Web, pero con claras diferencias por los menos GET Obtiene/solicita datos del servidor, se envian por clave=valor y es ideal para consultas.
# Mientras que post envia datos al servidor por ejemplo inicio de sesión, enviar formularios. Es mas seguro y dejas enviar mas información.

# if __name__=="__main__": # Inicia el servidor. Flask inicua el servidor con app.run()
# Debug=True Es una herramienta para desarrolladores que permite ver errores detallados y recargar automaticamente cuando se guardan cambios.


# PUNTO 12 ********************************************


# Plantillas HTML con Jinja2

# Que es Jinja2? es un motor de platillas de Flask, es una de sus gran herramientas. Su función es combinar el codigo python con html para crear paginas dinamicas.

# Carpeta TEMPLATE: Flask predeterminadamente una carpeta llamada templates donde busca los archivos HTML

# Para crear una carpeta templates existen dos formas: 
# La primera es la mas usada que es manualmente, creas la carpeta dentro de tu proyecto visual con 'templates' todo en miniscula
# La segunda manera es abriendo la terminal y escrbiendo 'mkdir templates' en ella.
# La tercera manera es crearla desde un codigo que la crea.

# Se importa un modulo en este caso 'os' que permite interactuar con el sistema dejando crear carpetas, renombrar archivos o acceder a rutas.

# Se usa la función makedirs() que crea uno o varias carpetas/directorios.
# exist_ok=True indica que si la carpeta ya existe, que el programa no genere error y continue.

# render_template() en ves de devolver un texto devuelve el archivo HTML
# Como primero se debe importar junto a flask.
# Se debe tener creada ya la carpeta de templates y como minimo un archivo html.
# render_template: Busca el archivo index.html dentro de templates y lo envia al navegador junto a la variable
# SINTAXIS Jinja2: {{variable}} se utiliza para mostrar el valor de una variables enviada desde flask.
# {% if %} se utiliza para evaluar una condición y mostrar el contenido segun se cumpla la condición o no.
# {%for%} recorre listas, tuplas o diccionarios.
# {% endfor %} finaliza un ciclo for.

# PUNTO 13 ********************************************

# Un formulario HTML con metodo post se utiliza para enviar info al servidor. Es comun para enviar contraseñas o formularios de registro.
# Primero se debe crear el archivo html y crear un formulario.
# Utilizamos el metodo POST Porque enviamos datos al servidor, y que se ejecutara cuando entremos en /guardar
# request contiene toda la info que envio el navegador y method dice que metodo se utilizo es este caso post

# request.form contiene los datos enviados por el formulario y el 'nombre' tiene que ser exacto al atributo de name= en HTML
# GET y POST métodos HTTP usados para comunicarse con servidores Web, pero con claras diferencias por los menos GET Obtiene/solicita datos del servidor, se envian por clave=valor y es ideal para consultas.
# Mientras que post envia datos al servidor por ejemplo inicio de sesión, enviar formularios. Es mas seguro y dejas enviar mas información.
# request.form permite acceder a los datos enviados desde un formulario HTML mediante el método POST.

# PUNTO 14 ********************************************

#  RUTAS CON VARIABLES: permiten recibir datos/parametros en las rutas y trabajar con ellos. Se llamas rutas variables porque una parte es fija(ruta) y la otra variable

# TIPOS DE CONVERSORES: por defecto todo lo que llega de la URL es un string.
# Flask permite indicar el tipo de dato que esperas con lo siguiente:
# @app.route("/usuario/<string:nombre>")  si es texto
# <int:id>" para dato numerico
#  <float:valor> para dato decimal. y si no recibe el tipo de dato que espera genera un error 404

#Parámetros de consulta  con request.args:se utiliza para acceder a los parametos enviados en la URL por medio de GET
# son diferentes a las rutas con variables porque en vez de escribir: /ubicación/<ciudad>, se escribe /buscar?ciudad=palmira (es un ejemplo) como parametos de consulta.

# request.args.get("ciudad","") busca el parametro ciudad, si no existe, devuelve una cadena vacia como valor predeterminado
# Son importantes proque son muy utilizados en APIs Rest y en Paginas web para mostar info dinamica  y responder a las solicitudes de los usuarios.

# PUNTO 15 ********************************************


# La carpeta static se usa para guardar archivos estaticos,osea archivos que no cambian segun las acciones del usuario.
# se suele guardar ahi los archivos css, javascript, imagenes, iconos, fuentes.

# La estructura del proyecto suele organizarse asi:
# carpeta del proyecto en si.
# el archivo app.py
# la carpeta de static que dentro tiene:
# -carpeta css: dentro todos los css.
# -carpeta js: todos los archivos js que se necesiten.
# -carpeta img: con las imagenes, iconos, etc.
# fuera de static, la carpeta de templates:
# - todos los html.



# se suele acceder a ellos por medio de la función url_for() en html
# <link rel="stylesheet" href="{{ url_for('static', filename='css/estilos.css') }}"> es para conectar un css a un html.
# permite mantiener un proyecto ordenado. la url_for genera la ruta correcta porque si se llega a cambiar la estructura del proyecto, flask seguira encontrando al archivo.

# <img src="{{ url_for('static', filename='img/logo.png') }}" alt="Logo"> se usa para las imagenes.
# <script src="{{ url_for('static', filename='js/script.js') }}"></script> para unir un archivo JS con el html.
# static indica la carpeta y filename= indica el archivo que necesitemos.

# ¿Por qué es importante?
# Todo sitio web necesita hojas de estilo, imágenes y archivos JavaScript. Organizar estos recursos en la carpeta static permite crear interfaces y mantener el proyecto organizado.

# PUNTO 16 ********************************************


# ¿Que es base.html? Es la plantilla que tiene las partes comunes de las paginas como el header, el navbar, footer o enlaces al css.

# {%extends %}: permite que una pagina utilice el contenido de base.html
# {% block %}: sección que puede ser reemplazada por las paginasa que utilicen a base.html. Espacio para que otra página escriba ahi su contenido.  
# {% block contenido %}: Es el bloque donde irá el contenido específico de cada página.

# PUNTO 17 ********************************************

# Que es redirect(): sirve para enviar al usuario automaticamente a otra ruta
# Ej: cuando se inicia sesión, Flask no te deja en el formulario si no que te manda a otra pagina.

# Que es url_for() Genera la url de una ruta Flask automaticamente.
# Es recomendado para no escribir manualmente las url porque si mañanas cambiamos la ruta en el @app.route tendremos que cambiar el redirect.
# Mientras que con url_for la encuentra solita sin modificar esa linea.
# redirect() redirige al usuario a otra ruta, en este caso a pagina.
# url_for() busca la ruta asociada a la función "pagina" y genera la URL automáticamente.
# ¿Por qué es importante?
# Después de procesar un formulario es común redirigir al usuario a otra página.
# La url_for() evita escribir las URLs manualmente, haciendo el proyecto más fácil de mantener si las rutas cambian.

# PUNTO 18 ********************************************

# Que es @app.errorhandler? es un decorador que permite manejar errores especificos.
 
# ERROR 404: "pagina no encontrada", sucede cuando se ejecuta una dirección que no existe.
# ERROR 500: "Error interno del servidor", sucede cuando el programa falla por un error inesperado mientras procesa la solicitud
# En vez de mostrar estos tipicos errores podemos mostrar paginas mas personalizadas.

# Es importante porque le da mas identidad a nuestra pagina y mejora la experiencia del usuario tambien hace que se vea mas profesional

# PUNTO 19 ********************************************

# Una sesión permite guardar información de un usuario mientras navega por la aplicación. Ej: nombre de usuario, preferencias o si ha iniciado sesión.
# SECRET_KEY: Es una clave secreta que Flask utiliza para proteger informacion almacenada en la sesióm.
# Es obligatoria si usamos session

# 'session' es un diccionario en el cual se pueden guardar datos y leer.
# session["usuario"]= "Laura"  es para guardar.
# usuario = session.get("usuario", "Invitado") si existe usuario devuelve laura, si no devuelve invitado.
# para cerrar 'session' se pueden utilizar dos maneras:
# session.pop("usuario") para eliminar un solo dato.
# session.clear() para eliminar toda la 'session'

# Es importante porque permite recordar la info del usuario entre distintas paginas.

# PUNTO 20 ********************************************

# Que es uan ApiRest? permite que diferentes apps se comuniquen entre si mediante solicitudes http (get, post, put, delete)
# Json es un formato para intercambiar datos, es facil de leer para personas y programas.
# jsonify() convierte listas o diccionarios de python a formato Json para enviarlos.

# para utlizarlo se tiene que importar jsonify y se puede utilizar para mensajes:
# return jsonify({"mensaje": "Hola Mundo"}) 
# o para enviar varias variables o listas,o lista de diccionarios:
# def usuario():
#   nombre = "Laura"
#    edad = 16
#    ciudad = "Cali"
#    return jsonify({
#        "nombre": nombre,
#        "edad": edad,
#        "ciudad": ciudad  })


# ENDPOINT: es una ruta de la API por la cual se recibe o devuelve información. En mi ejemplo deevuelven datos en formato json.

# Como probar la API? Se escribe en la ruta de navegación http://127.0.0.1:5000/api/direcciones o http://127.0.0.1:5000/api/empresa
# o se puede utilizar postman para enviar solicitudes http y ver las respuestas en formatos JSON.

# PUNTO 21 ********************************************

# sqlite3 es el modulo de python que permite crear y administrar bases de datos SQLite
# se importa con: import sqlite 
# Se crea la conexión con la base de datos y si mo exite SQlite lo crea automaticamente
# crea el cursor que es el encargado de ejecutar las consultas SQL

# CREATE TABLE crea una tabla donde se almacenarán los datos.
# IF NOT EXISTS evita que se produzca un error si la tabla ya existe.

# INSERT INTO: se suele utilzar para agregar nuevos registros a la tabla.
# SELECT consulta o recupera la info almacenada.
# commit() guarda permanentemente los cambios realizados en la base de datos.
# close() cierra la conexión con la base de datos.

# Es importantes pq permite guarda la info permanentemente, es utilizado en app pequeñas antes de trabajar con sistemas mas grandes.

# PUNTO 22 ********************************************
# Flask puede conectarse a una base de datos SQLite para guardar y consultar información.
# CRUD son las cuatro operaciones básicas que se realizan en una base de datos:
# C(Create): Crear o insertar nuevos registros.
# R(Read): Leer o consultar los registros.
# U(Update): Actualizar o modificar un registro.
# D(Delete): Eliminar un registro.

# Flask abre una conexion a la bd cada vez que le llega una solicitud del usuario y la cierra cuando la operación termina. Evita dejar conexiones abiertas y mejora el rendimiento

# Es importante porque permite guardar la info enviada desde los formularios y consultarla posteriormente.
# Es comun que se utilice en proyectos pequeños o medianos, ya que facilita el desarrollo de la web con base de datos.

# PUNTO 23 ********************************************
# Un entorno virtual es un espacio aislado donde se instalan las librerías de un proyecto sin afectar otros proyectos de Python.
# evita conflictos entre versiones de librerias. 
# Para crear un entorno virtual se escribe en la terminal: python -m venv venv
# para activar el venv en windows  source venv/bin/activate
# pip install flask Instala Flask  dentro del entorno virtual.
# Guardar todas las dependencias instaladas: pip freeze > requirements.txt
# Instalar las dependencias desde el archivo:  pip install -r requirements.txt

# PUNTO 24 ********************************************
# Git registra el historial de cambios de un proyecto. Investigue los comandos basicos: git init, git add, git commit, git status y la diferencia entre el area de trabajo y el repositorio.
# Iniciar repositorio
# git init
# Ver estado
# git status
# Agregar archivos al stage
# git add .
# Crear un commit
# git commit -m "Primera version del proyecto Flask"
# Ver historial
# git log --oneline
# Git permite llevar un historial de los cambios realizados en un proyecto, recuperar versiones anteriores, trabajar en equipo y compartir código de forma organizada. 

# PUNTO 25 ********************************************
# GitHub es una plataforma en línea donde se almacenan repositorios Git.Permite respaldar proyectos, trabajar en equipo y compartir código con otras personas.

# Cómo subir un proyecto a GitHub?
# Crear un repositorio en  la paginagithub
# Conectar el repositorio local.
# git remote add origin https://github.com/link que proporcione github
# git remote: administra los repositorios remotos.
# add: agrega un nuevo repositorio remoto.
# origin: nombre que recibe el repositorio remoto principal.
# https://github.com/...: dirección del repositorio creado en GitHub.
# Cambiar el nombre de la rama principal a main.
# git branch -M main
# branch: administra las ramas del proyecto.
# -M: cambia el nombre de la rama.
# main: nombre de la rama principal.
# Subir el proyecto a GitHub.
# git push -u origin main
# push: envía los cambios al repositorio remoto.
# -u: establece origin/main como referencia para futuros envíos.
# origin: repositorio remoto.
# main: rama que se enviará.
# Para subir cambios futuros:
# git add .
# git commit -m "Agrego ruta de productos"
# git push

# Por qué es importante?
# GitHub permite almacenar proyectos en la nube, compartir código,
# colaborar con otros desarrolladores y mantener un respaldo del trabajo. Tambien es portafolio profesional más utilizado por las empresas para conocer los proyectos y la experiencia de un desarrollador.

# PUNTO 26 ********************************************

# Estructura profesional de un proyecto Flask
# Un proyecto Flask organiza los archivos en carpetas para mantener el código ordenado, facilitar su mantenimiento y permitir que otros desarrolladores comprendan el proyecto fácilmente.
# app.py
# Es el archivo principal de la aplicación. Contiene la configuración, las rutas y la lógica del servidor.
# templates/
# Carpeta donde se almacenan los archivos HTML que Flask renderiza mediante render_template().
# static/
# Contiene los archivos estáticos como hojas de estilo CSS, archivos JavaScript, imágenes, íconos y fuentes.

# requirements.txt
# Guarda la lista de dependencias del proyecto para poder instalarlas posteriormente con el comando:
# pip install -r requirements.txt

# .gitignore
# Indica a Git qué archivos o carpetas no deben subirse al repositorio, por ejemplo el entorno virtual (venv), archivos temporales o bases de datos.

# README.md
# Es un documento que describe el proyecto, explica su funcionamiento, requisitos, instalación y forma de uso.

# Una estructura organizada facilita el mantenimiento del proyecto, permite que otros desarrolladores comprendan el código rápidamente y sigue las buenas prácticas utilizadas en proyectos profesionales con Flask.

# PUNTO 27 ********************************************
# Es un archivo que le indica a Git qué archivos o carpetas no debe
# guardar ni subir al repositorio.
# ¿Qué archivos se suelen ignorar en proyectos Python/Flask?
# venv/
# Contiene el entorno virtual y puede ser recreado en cualquier computador.
# __pycache__/
# Guarda archivos temporales generados automáticamente por Python.
# *.db
# Ignora las bases de datos SQLite si no se desean compartir.
# *.pyc
# Archivos compilados de Python.
# .env
# Suele contener información privada como contraseñas o claves de acceso.
# ¿Qué es README.md?
# Es un archivo escrito en Markdown (.md) que documenta el proyecto.
# Explica de qué trata, cómo instalarlo, cómo ejecutarlo y qué tecnologías utiliza.