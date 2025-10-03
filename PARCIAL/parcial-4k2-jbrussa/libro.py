from material import Material

class Libro(Material):
    tipo = 1
    def __init__(self, codigo, titulo, autor, precio_base, dias_prestados):
        super().__init__(codigo, titulo, autor, precio_base)
        self._dias_prestados = int(dias_prestados)

    @property
    def dias_prestados(self):
        return self._dias_prestados
    @dias_prestados.setter
    def dias_prestados(self, value):
        self._dias_prestados = int(value)

    def calcular_costo_mantenimiento(self):
        # $100 por cada 30 días prestados (cada fracción cuenta como período completo)
        periodos = (self._dias_prestados + 29) // 30
        if periodos < 1:
            periodos = 1
        return periodos * 100
