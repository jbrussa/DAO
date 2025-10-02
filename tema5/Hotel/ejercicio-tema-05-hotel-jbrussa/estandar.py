from habitacion import Habitacion


class Estandar(Habitacion):
    tipo = 1

    def __init__(self, numero: int, huesped: str, costo_base: float, noches: int, extra: bool = False):
        super().__init__(numero, huesped, costo_base, noches)
        # Para estándar el campo extra se mantiene pero no se utiliza
        self._extra = bool(extra)

    def calcular_costo(self) -> float:
        return self.costo_base * self.noches
