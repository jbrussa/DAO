

class Equipo:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.cantidadDePartidosJugados = 0
        self.cantidadDePartidosLocal = 0
        self.cantidadDePartidosVisitante = 0
        self.golesRealizados = 0
        self.golesRecibidos = 0
        self.diferenciaDeGoles = 0
        self.partidosGanados = 0
        self.partidosEmpatados = 0
        self.partidosPerdidos = 0

    
    def registrarPartido(self, partido) -> None:
        ## Métricas
        self.cantidadDePartidosJugados += 1
        if partido.equipoLocal.nombre == self.nombre:
            self.cantidadDePartidosLocal += 1
            self.golesRealizados += partido.golEquipoLocal
            self.golesRecibidos += partido.golEquipoVisitante
            if partido.definicionPartido() == {self.nombre}:
                self.partidosGanados += 1
            elif partido.definicionPartido() is None:
                self.partidosEmpatados += 1
            else:
                self.partidosPerdidos += 1
        else:
            self.cantidadDePartidosVisitante += 1
            self.golesRealizados += partido.golEquipoVisitante
            self.golesRecibidos += partido.golEquipoLocal
            if partido.definicionPartido() == {self.nombre}:
                self.partidosGanados += 1
            elif partido.definicionPartido() is None:
                self.partidosEmpatados += 1
            else:
                self.partidosPerdidos += 1
        self.diferenciaDeGoles = self.golesRealizados - self.golesRecibidos
        self.puntos = 3 * self.partidosGanados + 1 * self.partidosEmpatados

    def __str__(self) -> str:
        return f"Equipo: {self.nombre} \n ========== \n Partidos Jugados: {self.cantidadDePartidosJugados}\n Partidos Local: {self.cantidadDePartidosLocal} \n Partidos Visitante: {self.cantidadDePartidosVisitante} \n Goles Realizados: {self.golesRealizados} \n Goles Recibidos: {self.golesRecibidos} \n Diferencia de Goles: {self.diferenciaDeGoles} \n Partidos Ganados: {self.partidosGanados} \n Partidos Empatados: {self.partidosEmpatados} \n Partidos Perdidos: {self.partidosPerdidos} \n Puntos: {3 * self.partidosGanados + 1 * self.partidosEmpatados} \n \n"

