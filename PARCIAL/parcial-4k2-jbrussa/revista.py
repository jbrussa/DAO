from material import Material

class Revista(Material):
    tipo = 3
    def __init__(self, codigo, titulo, autor, precio_base, origen):
        super().__init__(codigo, titulo, autor, precio_base)
        self._origen = origen.lower()

    @property
    def origen(self):
        return self._origen
    @origen.setter
    def origen(self, value):
        self._origen = value.lower()

    def calcular_costo_mantenimiento(self):
        # $50 por ejemplar, +20% si importada
        base = 50
        if self._origen == "importada":
            return base * 1.2
        return base
