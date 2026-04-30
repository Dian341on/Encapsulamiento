"""Crea una clase llamada Estudiante que tenga atributos como nombre, edad y notas (una lista de números).
Implementa métodos para agregar una nota y calcular el promedio de las notas. """


class Estudiante: 
    def __init__ (self, nombre, edad ):
        self.nombre = nombre
        self.edad = edad 
        self.notas = []
    
    def agregar_notas(self, nota):
        
        self.notas.append(nota)
        
    def promedio_notas( self): 
        if len (self.notas) == 0:
            return 0
        return sum (self.notas) / len (self.notas)
            