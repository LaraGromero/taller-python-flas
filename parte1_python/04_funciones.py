# Funciones — def, parámetros, return

#¿Que son las funciones? Son bloques de codigo que realizan una tarea específica, reducen la repetición de codigo. Son como un bloque con instrucciones que se peude reutilizar.

#Como se define una función? Se define con la palabra reservada 'def' seguida del nombre de la función y paréntesis. 

def direccion(): #Definimos la función 'direccion' con la palabra reservada 'def' y los paréntesis.
    print("Tu dirección es: Calle 123") #Dentro de la función se coloca el bloque de código que queremos que se ejecute cuando llamemos a la función.
    
direccion()
#Que es un parámetro? Es una variable que se define dentro de la función y recibe unos valores especificos.

def direccion_parametro(calle, numero): #Definimos la función 'direccion_parametro' con dos parámetros 'calle' y 'numero'. 
    print(f"Tu dirección es: {calle} {numero}") #Dentro de la función se coloca el código que queremos que se ejecute cuando la llamemos donde utilize los parámetros.
    
direccion_parametro(28,28-56)
#Valores por defecto son los cuales se asignan a los parametros en caso de que el usuario no ingrese un valor.

def mostrar_edad(edad=18): #Definimos la función 'mostrar_edad' con un parámetro 'edad' y le asignamos un valor por defecto de 18.
    # print(f"Tu edad es: {edad}") #Dentro de la función se coloca el código que queremos que se ejecute cuando la llamemos donde utilize el parámetro.
    return edad #La palabra reservada 'return' nos permite devolver un valor desde la función, en este caso el valor del parámetro 'edad'.

mostrar_edad(24)
# Return entrega un valor para seguir trabajando con él. Mientras que print muestra el valor en la pantalla. 
