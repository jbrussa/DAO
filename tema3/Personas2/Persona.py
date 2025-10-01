
class Persona(object):
    def __init__(self, documento: int, nombre: str, apellido: str, edad: int) -> None:
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self) -> str:
        return f"{self.documento}: Hola, mi nombre es {self.nombre} y tengo {self.edad} años"
    
    def es_mayor_de_edad(self) -> bool:
        return self.edad >= 18
        
    def es_vocal_apellido(self) -> bool:
        return self.apellido[0].lower() in "aeiou"
    
