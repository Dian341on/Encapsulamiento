"""a una clase llamada Persona con atributos nombre, edad y sexo.
Implementa un método que permita cambiar la edad de la persona y otro
que muestre la información de la persona."""

class Persona:
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre  
        self.edad = edad      
        self.sexo = sexo

        def establecer_edad( self, edad):
            self.edad = edad
            
        def mostrar_datos (self) :
            print ( f"Persona: {self.nombre}, Edad: {self.edad} , sexo {self.sexo} " )
