#Manejo de Archivos — open, read, write

#OPEN() basicamente es como abrir el archivo para poder trabajar con el.
    
#'r' (read) modo de apertura, el cual hace que lea el archivo no lo modifica.
#'w' (write)  escribe pero si el archivo ya tenia contenido, borra y escribe de nuevo.
#'a' (append) agrega información al final del documento.

# Metodos.
# with permite que el archivo se cierre automaticamente al terminar. 
#write() permite escribir dentro de un archivo que ya fue abierto.
#para leer linea por linea se suele usar for.
#strip() en el taller aparece como ejemplo, su proposito es quitar espacios y saltos de linea sobrantes.

with open("estudiantes.txt", "w") as archivo: #Lo que hace es abrir el archivo, con 'w' si hay contenido borra y escribe o lo crea si no existe.
    archivo.write("Laura\n") #Aqui empezamos a escribir dentro del archivo
    
with open("estudiantes.txt", "a") as archivo: # con 'a' agrega al final.
    archivo.write("Santiago\n") #Aqui empezamos a escribir.

    
with open("estudiantes.txt", "r") as archivo: #'r' abre para leer.
    for est in archivo: #recorre cada linea
        print (est.strip()) #Elimina los saltos de linea que hayan dentro del archivo