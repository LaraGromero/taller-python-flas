# Ciclos — for y while

carros=["Ford", "McLaren", "Ferrari", "Chevrolet"]

for marca in carros: # Basicamente el ciclo for recorre cada elemento de la lista y le asigna la variable 'marca' para luego imprimirla.
    print(marca) 
    
print ("*******")

x= 3
multi =0
while multi < 10: # Mientras multi sea menor a 10, se ejecutará el ciclo while.
    print (f"{x}*{multi} = {x * multi}") # Imprime el resultado de la multiplicación de x por multi.
    multi +=1 #Esta linea es la que hace que el ciclo avance porque incremente el valor de multi sumandole un uno cada vez que se cumpla el ciclo. 
    
print ("*******")

objetos=["Mesa", "Silla", "Cama", "Escritorio"] #Lista.

for objeto in objetos: # Recorre cada elemento de la lista 'objetos'.
    if objeto == "Cama": #Si encuentra el objeto "Cama" detiene el ciclo.
        break 
    print(objeto) # Imprime los objetos hasta que encuentra "Cama", luego se detiene el ciclo.
    
print ("*******")
for objeto in objetos: # Recorre cada elemento de la lista 'objetos'.
    if objeto == "Cama": #Si encuentra el objeto "Cama" salta a la siguiente iteración del ciclo.
        continue 
    print(objeto) # Imprime los objetos, pero cuando encuentra "Cama" no lo imprime y continúa con el siguiente objeto.

