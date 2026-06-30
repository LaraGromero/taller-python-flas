# Estructuras de Control — if, elif, else

#If se utiliza para ejecutar un bloque de código si una condición es verdadera. Un ejemplo en la vida cotidiana seria:
#Quiero comprar un helado, pero solo si tengo dinero. ¿Tengo dinero? Si, compro el helado. ¿Tengo dinero? No, no compro el helado.

tengo_dinero = True #Creamos una variable booleana que indica si tenemos dinero o no.
if tengo_dinero == True: # Si la variable tengo_dinero es igual a True, entonces se ejecuta el codigo dentro del if.
    print("Compro el helado")
else: #Si no es asi, entonces se ejecuta el código dentro del else.
    print("No compro el helado")
    

notas= 4.0 #Creamos una variable que almacena la nota del examen.
if notas >= 4.5:
    print("Excelente") 
elif notas >= 3.5: #Lo que hace es si notas no aplica para if, entonces se mira si aplica para elif, y asi sucesivamente hasta que se cumpla una condicion o se llegue al else.
    print("Regular")
else:
    print("Insuficiente")
    

edad= 17
if edad >= 18:
    print("Adulto")
elif edad >= 13 and edad < 18: #Aqui se utiliza el operador logico 'and' para combinar dos condiciones, donde ambas deben cumplirse para que se ejecute el bloque de código.
    print("Adolescente")
else:
    print("Niño")