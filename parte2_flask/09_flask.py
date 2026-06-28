#Que es Flask y como instalarlo

#¿QUE ES UN FRAMEWORK? En pocas palabras son las herramientas y estructuras ya hechas para el desarrollo de aplicativos.
#Ej cotidiano: al construir una casa necesitamos planos, herramientas eso es un framework.

#¿QUE ES UN MICROFRAMEWORK? Como lo dice la palabra MICRO trae cosas mas sencillas y esenciales de un framework normal. 
#Flask es considerado un MICROframework porque es flexible, sencillo, tiene pocas herramientas integradas.

#DIFERENCIAS CON DJANGO
#Django es un framework desde ahi esta la diferencias porque al ser un framework esta mas completo, tiene mas herramientas, es mas pesado, recomendado para proyectos grandes.

#Como instalar Flask

#En tu terminal escribres:

#pip install flask 

#Pip es el gestor de paquetes de Python, lo solemos utilizar para instalar librerias.


#Para verificar tenemos dos maneras totalmente validas que nos dan el mismo resultado.
import flask; 
print(flask.__version__) #3.1.2 dice esto en la terminal

#python -c "import flask; print(flask.__version__)" escribir esto en tu terminal que arroja a lo mismo