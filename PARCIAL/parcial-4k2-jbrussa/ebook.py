from material import Material

class Ebook(Material):
    tipo = 2
    def __init__(self, codigo, titulo, autor, precio_base, valor_venta):
        super().__init__(codigo, titulo, autor, precio_base)
        self._valor_venta = float(valor_venta)

    @property
    def valor_venta(self):
        return self._valor_venta
    @valor_venta.setter
    def valor_venta(self, value):
        self._valor_venta = float(value)

    def calcular_costo_mantenimiento(self):
        # 5% sobre el valor de venta
        return round(self._valor_venta * 0.05, 2)
