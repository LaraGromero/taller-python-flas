#PROGRAMACIÓN ORIENTADA A OBJETOS
#Forma de estructura de programas el cual se centra en programar objetos o entidades del mundo real.
#Basicamente: Un objeto tiene caracteristicas y comportamientos. 
#Clase es como un molde para crear muchas instancias

class Animal: #class es reservada para crear clase, primero se llama y luego se nombra con lo eligamos.
    def __init__(self, nombre, tipo, edad): #es el constructor de la clase, ejecuta automáticamente cuando se crea un objeto y sirva para definir los atributos
        self.nombre= nombre
        self.tipo= tipo #Self hace referencia al objeto/instancia. Son las características o datos que pertenecen a cada objeto creado a partir de la clase.
        self.edad= edad
        
    def metodo(self): #Son funciones definidas dentro de una clase que permiten realizar acciones o trabajar con los atributos del objeto.
        print(f"{self.nombre}, es un {self.tipo} Y tiene {self.edad} años") #En este caso lo utilizo mostrando la info 
        print (f"{self.nombre} corre\n{self.nombre} come") #Y aqui sus comportamientos.
        
        
animal1= Animal("Firulais","Conejo",3)
# print (animal1.metodo()) Esta manera de mostrar los datos con print aparece None porque hace print a una función que no devuelve nada. 
animal1.metodo() #Manera correcta
