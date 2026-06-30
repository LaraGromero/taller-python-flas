#Archivos estaticos — CSS, JS e imagenes

#La carpeta static se usa para guardar archivos estaticos,osea archivos que no cambian segun las acciones del usuario.
#se suele guardar ahi los archivos css, javascript, imagenes, iconos, fuentes.

#La estructura del proyecto suele organizarse asi:
#carpeta del proyecto en si.
#el archivo app.py
#la carpeta de static que dentro tiene:
# -carpeta css: dentro todos los css.
# -carpeta js: todos los archivos js que se necesiten.
# -carpeta img: con las imagenes, iconos, etc.
#fuera de static, la carpeta de templates:
# - todos los html.



#se suele acceder a ellos por medio de la función url_for() en html
#<link rel="stylesheet" href="{{ url_for('static', filename='css/estilos.css') }}"> es para conectar un css a un html.
# permite mantiener un proyecto ordenado. la url_for genera la ruta correcta porque si se llega a cambiar la estructura del proyecto, flask seguira encontrando al archivo.

# <img src="{{ url_for('static', filename='img/logo.png') }}" alt="Logo"> se usa para las imagenes.
# <script src="{{ url_for('static', filename='js/script.js') }}"></script> para unir un archivo JS con el html.
# static indica la carpeta y filename= indica el archivo que necesitemos.

# ¿Por qué es importante?
# Todo sitio web necesita hojas de estilo, imágenes y archivos JavaScript. Organizar estos recursos en la carpeta static permite crear interfaces y mantener el proyecto organizado.