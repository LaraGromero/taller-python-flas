#PUNTO 1: VARIABLES Y TIPO DE DATO.
# ¿Que es una variable? Una variable es basicamente una caja donde se puede guardar información y esta utiliza una etiqueta para poder identificarla. 

nombre= "Laura" #En este caso la etiqueta es 'nombre' y el valor que tiene es "Laura"
print (nombre) #En este caso se imprime el valor de la variable 'nombre' que es "Laura"

# Las variables pueden almacenar diferentes tipos de datos, como números, texto, booleanos, entre otros. Estos suelen ser los mas comunes.

edad= 25 #En este caso la etiqueta es 'edad' y el valor que tiene es 25, y es valor tipo de dato entero (int).
print (type(edad))#Esto nos permite ver el tipo de dato que tiene la variable 'edad' en este caso es int.
fruta= "Manzana" #En este caso la etiqueta es 'fruta' y el valor que tiene es "Manzana", y es valor tipo de dato cadena de texto (str).
print (type(fruta))
nota= 3.4 #En este caso la etiqueta es 'nota' y el valor que tiene es 3.4, y es valor tipo de dato decimal (float)
print (type(nota))
activo= True #En este caso la etiqueta es 'activo' y el valor que tiene es True, y es valor tipo de dato booleano (bool).
print (type(activo))

#¿Que es tipado dinamico? Python brinda una flexibilidad al permitir que una variables pueda cambiar de tipo durante el programa, donde puede empezar siendo un tipo de dato (str) 
#y luego podemos cambiarlo a dato entero.
nombre= "Pepito"
print (type(nombre)) 
nombre= 30
print (type(nombre)) 
