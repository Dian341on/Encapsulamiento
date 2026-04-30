"""Crea una clase llamada Libro con atributos titulo, autor y año_publicacion. 
Implementa un método que devuelva una descripción del libro y otro que verifique 
si el libro es considerado un clásico (publicado hace más de 50 años)."""

from datetime import datetime

class Libro: 
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        
    def descripcion (self):
        
        return f"'{self.titulo}' es del autor {self.autor}, que fue publicado en el año {self.anio_publicacion}"
        
    def es_clasico (self):
        
        anio_actual = datetime.now().year
        return (anio_actual - anio_publicacion) >50
        
        
        
