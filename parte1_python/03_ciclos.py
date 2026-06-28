# Ciclos — for y while

#Que son los ciclos?
# Los ciclos son estructuras de control que permiten repetir un bloque de código varias veces.
# La repetición puede depender de una condición (while) o de una colección de elementos (for). Ademas ayudan a reducir la repetición de codigo haciendo los programas mas cortos y faciles.

#DIFERENCIA ENTRE FOR Y WHILE
# FOR: Se utiliza cuando necesito recorrer cada elemento de una lista, tupla o cadena de texto, porque ya conozco los elementos que voy a recorrer.
carros=["Ford", "McLaren", "Ferrari", "Chevrolet"]

for marca in carros: # Basicamente el ciclo for recorre cada elemento de la lista y le asigna la variable 'marca' para luego imprimirla.
    print(marca) 
    
print ("*******")
#WHILE: cuando necesito repetir una acción hasta que se cumpla una condición determinada. 
# Por ejemplo, un contador, una calculadora, un menú o la solicitud de datos al usuario hasta que ingrese una respuesta válida.

x= 3
multi =0
while multi < 10: # Mientras multi sea menor a 10, se ejecutará el ciclo while.
    print (f"{x}*{multi} = {x * multi}") # Imprime el resultado de la multiplicación de x por multi.
    multi +=1 #Esta linea es la que hace que el ciclo avance porque incremente el valor de multi sumandole un uno cada vez que se cumpla el ciclo. 
    
print ("*******")
#Break: se utiliza para salir de un ciclo cuando se cumple una condición determinada. Detiene completamente el ciclo.

objetos=["Mesa", "Silla", "Cama", "Escritorio"] #Lista.

for objeto in objetos: # Recorre cada elemento de la lista 'objetos'.
    if objeto == "Cama": #Si encuentra el objeto "Cama" detiene el ciclo.
        break 
    print(objeto) # Imprime los objetos hasta que encuentra "Cama", luego se detiene el ciclo.
    
print ("*******")
#Continue: se utiliza para saltar a la siguiente iteración del ciclo cuando se cumple una condición determinada. 

for objeto in objetos: # Recorre cada elemento de la lista 'objetos'.
    if objeto == "Cama": #Si encuentra el objeto "Cama" salta a la siguiente iteración del ciclo.
        continue 
    print(objeto) # Imprime los objetos, pero cuando encuentra "Cama" no lo imprime y continúa con el siguiente objeto.

