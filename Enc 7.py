"""Crea una clase llamada Empleado con atributos nombre,
salario y departamento. Implementa un método que aumente el salario
en un porcentaje dado y otro que muestre la información del empleado."""

class Empleado:
    def __init__(self, nombre, salario, departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento
    
    def aumento_salario (self, salario):
        
        return salario + salario * (cantidad /100) 
        
    def informacion_empleado (self):
    
         return f"informacion_empleado: {self.nombre} {self.salario}, departamento: {self.departamento}"
        
        