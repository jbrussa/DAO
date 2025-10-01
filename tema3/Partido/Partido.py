from Equipo import Equipo

class Partido:
    def __init__(self, equipoLocal: Equipo, equipoVisitante: Equipo, golEquipoLocal = 0, golEquipoVisitante = 0 ):
        self.equipoLocal = equipoLocal
        self.equipoVisitante = equipoVisitante
        self.golEquipoLocal = golEquipoLocal
        self.golEquipoVisitante = golEquipoVisitante
    
    def __str__(self):
        return f"Partido entre {self.equipoLocal.nombre} y {self.equipoVisitante.nombre}. Goles: {self.golEquipoLocal}-{self.golEquipoVisitante}"

    def sumarGolEquipoLocal(self):
        self.golEquipoLocal += 1
        return self.golEquipoLocal
    
    def sumarGolEquipoVisitante(self):
        self.golEquipoVisitante += 1
        return self.golEquipoVisitante
    
    def definicionPartido(self):
        if self.golEquipoLocal > self.golEquipoVisitante:
            return {self.equipoLocal}
        elif self.golEquipoVisitante > self.golEquipoLocal:
            return {self.equipoVisitante}
        else:
            return None
   
