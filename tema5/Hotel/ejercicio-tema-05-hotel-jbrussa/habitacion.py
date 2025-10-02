
from abc import ABC, abstractmethod

class Habitacion(ABC):
    def __init__(self, numero: int, huesped: str, costo_base: float, noches: int):
        self._numero = int(numero)
        self._huesped = huesped
        self._costo_base = float(costo_base)
        self._noches = int(noches)

    # getters / setters
    @property
    def numero(self) -> int:
        return self._numero

    @numero.setter
    def numero(self, value: int) -> None:
        self._numero = int(value)

    @property
    def huesped(self) -> str:
        return self._huesped

    @huesped.setter
    def huesped(self, value: str) -> None:
        self._huesped = value

    @property
    def costo_base(self) -> float:
        return self._costo_base

    @costo_base.setter
    def costo_base(self, value: float) -> None:
        self._costo_base = float(value)

    @property
    def noches(self) -> int:
        return self._noches

    @noches.setter
    def noches(self, value: int) -> None:
        self._noches = int(value)

    @property
    def tipo(self) -> int:
        return getattr(self.__class__, "tipo", None)
    
    @abstractmethod
    def calcular_costo(self) -> float:
        """Calcula el costo total de la reserva. Implementado por subclases."""
        raise NotImplementedError()
