"""Crea una clase llamada Rectángulo que tenga atributos base y altura.
Implementa métodos para calcular el área y el perímetro del rectángulo. """

class rectángulo:
    def __init__(self, base, altura): 
        self.base= base
        self.altura=altura
    
    def calcular_area (self):
        
        return (self.base * self.altura )
        
    def calcular_perimetro (self):
        
        return (self.base * 2 ) + (self.altura + 2) 