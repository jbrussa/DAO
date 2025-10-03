from abc import ABC, abstractmethod


class Material(ABC):
    def __init__(self, codigo: str, titulo: str, autor: str, precio_base: float):
        self._codigo = codigo
        self._titulo = titulo
        self._autor = autor
        self._precio_base = float(precio_base)

    @property
    def codigo(self):
        return self._codigo
    @codigo.setter
    def codigo(self, value):
        self._codigo = value

    @property
    def titulo(self):
        return self._titulo
    @titulo.setter
    def titulo(self, value):
        self._titulo = value

    @property
    def autor(self):
        return self._autor
    @autor.setter
    def autor(self, value):
        self._autor = value

    @property
    def precio_base(self):
        return self._precio_base
    @precio_base.setter
    def precio_base(self, value):
        self._precio_base = float(value)

    def calcular_costo_mantenimiento(self):
        raise NotImplementedError()
