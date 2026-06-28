# Listas, Tuplas y Diccionarios

#LISTA: Se crea nombrando una variable y encerrando los elementos entre []. Es uno de los tipos de datos mas utilizados porque sus datos los podemos cambiar.

lista= ["rojo","verde","azul"] #Se crea

#Para acceder a ellas necesitamos tener en cuenta las posiciones donde "rojo" es nuestro primer elemento pero tiene la posición 0.

print (lista[1]) #Aqui mando a imprimir el elemento que este en la posición 1 en este caso seria verde. 

#para modificar tambien usaremos lo de las posiciones, llamarelos la lista y la posición y le asignamos un nuevo valor.
lista[0]= "rosado"
print (lista)

#para agregar nuevos elementos a una lista se usa .append que solo puede agregar de un elemento.
lista.append("rojo") #se coloca el valor nuevo entre ()
print (lista)

#para recorrer usariamos for.
for color in lista:
    print(color)
    
    
#TUPLAS: Son parecidas a la listas pero no se pueden cambiar sus valores sirven para valores especificos como fechas de nacimientos, registros de pagos, etc.
#Utiliza parentesis en vez de corchetes.
tupla= ("00001", "00002", "00003") #Se crea

print (tupla[1]) #Tambien para acceder a ellas se usa posiciones.

for id in tupla:
    print(id)  #Tambien se puede usar for para recorrerla.
    
    
#DICCIONARIO permite almacenar una clave con un dato. Las claves deben ser unicas, inmutables y tipo string y entero. Se puede agregar diccionarios, listas, cadenas y se define {}

factura= { 
    "nombre":"Laura",  #es necesario que esten separadas por : porque indica el valor de la clave y separadas por una , para saber donde termina la clave
    "id":1,
    "producto":"secador",
    "total":56000
}

print(factura)

# Para acceder llamamos el diccionario y entre [] escribimos la clave.

print(factura["nombre"]) 
print(factura["id"]) 

#PARA MODIFICAR

factura["nombre"]= "Santiago"

#PARA AGREGAR

factura["ciudad"]= "Palmira"

#Para recorrer tenemos que usar for que vuelve 

for clave in factura:
    print (clave)
    
for valor in factura.values():
    print (valor)
    
for clave, valor in factura.items(): #Agarra cada par del diccionario y los separa.
    print(clave, valor) #Es lo mas usado para recorrer claves y valores al mismo tiempo
