#Manejo de Excepciones — try, except, finally
# Resuelve problemas que hagan que el programa se detenga y genere error. Evita que el programa se detenga por errores y permite dar mensajes claros o tomar acciones correctivas.

#TRY: aqui se suele colcar codigos que podrian fallar
#EXCEPT: Se ejecuta si ocurre un error para corregirlo y evitar que el programa se detenga. Captura errores
#ValueError es una de las excepciones especificas y un ejemplo claro es cuando un usuaria digita un tipo de dato incorrecto, "hola" donde debia ir un dato numerico.
#ZeroDivisionError existe para evitar o ignorar las divisiones por 0
#finally: Su proposito es ejecutar un codigo haya error o no. Su uso típico es para liberar recursos o cerrar conexiones que se hayan abierto en Try.
#IndexError: Sucede cuando piden una posición que no existe

#Ejemplo sobre como iria su estructura en la vida real: 
# Try: Intentar abrir una puerta, pero esta cerrada.
#Except: Usar otra puerta.
#finally: Cerrar la puerta.


try: #Intenta lo siguiente
   edad= int(input("ingrese su edad: ")) #Pedimos al usuario el dato
   print (f"Su edad es: {edad}") #Lo imprimo si no existe error

except ValueError: #Si el usuario coloco un dato diferente al numerico hace lo siguiente.
    print("Error debes ingresar un dato numerico")
finally: #Codigo que si o si se va a ejecutar
    print(f"Gracias por usar este programa") 
    

    
   