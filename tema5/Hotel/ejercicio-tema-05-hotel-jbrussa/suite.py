from habitacion import Habitacion


class Suite(Habitacion):
    tipo = 2

    def __init__(self, numero: int, huesped: str, costo_base: float, noches: int, vista_mar: bool = False):
        super().__init__(numero, huesped, costo_base, noches)
        self._vista_mar = bool(vista_mar)

    @property
    def vista_mar(self) -> bool:
        return self._vista_mar

    @vista_mar.setter
    def vista_mar(self, value: bool) -> None:
        self._vista_mar = bool(value)

    def calcular_costo(self) -> float:
        factor = 1.10 if self.vista_mar else 1.0
        return self.costo_base * self.noches * factor
