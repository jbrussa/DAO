from abc import ABC, abstractmethod

class Atencion(ABC):
    def __init__(self, codigo, tipo_cobro):
        self._codigo = codigo  # Código numérico que identifica la atención
        self._tipo_cobro = tipo_cobro  # 1: efectivo, 2: tarjeta de crédito

    # Getter y setter para codigo
    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        self._codigo = valor

    # Getter y setter para tipo_cobro
    @property
    def tipo_cobro(self):
        return self._tipo_cobro

    @tipo_cobro.setter
    def tipo_cobro(self, valor):
        self._tipo_cobro = valor

    @abstractmethod
    def importeACobrar(self):
        pass