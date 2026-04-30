"""Crea una clase llamada Producto que tenga atributos nombre, precio y stock.
Implementa métodos para aumentar y disminuir el stock,
asegurándote de que no se pueda tener un stock negativo."""

class Producto:
    
    def __init__ (self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = 0.0
        
    def aumentar_stock (self, stock):
        self.stock = stock + aumento
        return self.stock
        
    def disminuir_stock (self,stock):
        self.stock = stock - disminuir
        if self.stock < 0.0 :
            print ("llegaste al limite chaval")
        else:
            return self.stock