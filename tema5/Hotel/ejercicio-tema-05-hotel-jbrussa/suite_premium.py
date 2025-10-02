from habitacion import Habitacion


class SuitePremium(Habitacion):
    tipo = 3

    def __init__(self, numero: int, huesped: str, costo_base: float, noches: int, jacuzzi: bool = False):
        super().__init__(numero, huesped, costo_base, noches)
        self._jacuzzi = bool(jacuzzi)

    @property
    def jacuzzi(self) -> bool:
        return self._jacuzzi

    @jacuzzi.setter
    def jacuzzi(self, value: bool) -> None:
        self._jacuzzi = bool(value)

    def calcular_costo(self) -> float:
        factor = 1.20 if self.jacuzzi else 1.0
        return self.costo_base * self.noches * factor
