# Estructuras de Control — if, elif, else

#If se utiliza para ejecutar un bloque de código si una condición es verdadera. Un ejemplo en la vida cotidiana seria:
#Quiero comprar un helado, pero solo si tengo dinero. ¿Tengo dinero? Si, compro el helado. ¿Tengo dinero? No, no compro el helado.

tengo_dinero = True #Creamos una variable booleana que indica si tenemos dinero o no.
if tengo_dinero == True: # Si la variable tengo_dinero es igual a True, entonces se ejecuta el codigo dentro del if.
    print("Compro el helado")
else: #Si no es asi, entonces se ejecuta el código dentro del else.
    print("No compro el helado")
    

#Else se utiliza para ejecutar si la condición no cumple con if ni con elif.
    
# Elif se utiliza para agregar condiciones adicionales a un bloque if. Un ejemplo en la vida cotidiana seria: 
#Para sacar un exelente en un examen debo sacar mayor o igual a 4.5, para sacar regular debo sacar mayor o igual a 3.5, y para sacar insuficiente debo sacar menor a 3.5.

notas= 4.0 #Creamos una variable que almacena la nota del examen.
if notas >= 4.5:
    print("Excelente") 
elif notas >= 3.5: #Lo que hace es si notas no aplica para if, entonces se mira si aplica para elif, y asi sucesivamente hasta que se cumpla una condicion o se llegue al else.
    print("Regular")
else:
    print("Insuficiente")
    
#Para la identación es muy importante que despues de cada if, elif y else se deben colocar ':' y 4 espacios para seguir escribiendo el codigo correspondiente a cada bloque.
#Ademas todos los if, elif y else deben estar alineados al mismo nivel. Ejemplo de mal:


# if tengo_dinero == True: 
# print("Compro el helado") #Aqui da error y debe estar alineado con los 4 espacios de identación.
# else: #Si no se colocan los ':' al final de cada if, elif y else, tambien dara error porque ese es el simbolo que indica el inicio de un bloque de código.
#     print("No compro el helado")

#COMPARACIÓN DE VALORES: Para ejecutar un bloque de código si una condición es verdadera, se utilizan operadores de comparación. Los operadores de comparación son los siguientes:
# ==   igual que
# !=   diferente de
# >    mayor que
# <    menor que
# >=   mayor o igual
# <=   menor o igual

#INCLUYO LOS CONECTORES LOGICOS: Para combinar varias condiciones, se utilizan operadores lógicos. Los operadores lógicos son los siguientes:
# and  y
# or   o


edad= 17
if edad >= 18:
    print("Adulto")
elif edad >= 13 and edad < 18: #Aqui se utiliza el operador logico 'and' para combinar dos condiciones, donde ambas deben cumplirse para que se ejecute el bloque de código.
    print("Adolescente")
else:
    print("Niño")