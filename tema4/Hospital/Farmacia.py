from Atencion import Atencion

class Farmacia(Atencion):
    def __init__(self, codigo, tipo_cobro, importe_medicamentos, cupon_descuento):
        super().__init__(codigo, tipo_cobro)
        if cupon_descuento < 0:
            raise ValueError("El cupón de descuento debe ser 0 o positivo")
        self._importe_medicamentos = importe_medicamentos
        self._cupon_descuento = cupon_descuento

    @property
    def importe_medicamentos(self):
        return self._importe_medicamentos

    @importe_medicamentos.setter
    def importe_medicamentos(self, valor):
        self._importe_medicamentos = valor

    @property
    def cupon_descuento(self):
        return self._cupon_descuento

    @cupon_descuento.setter
    def cupon_descuento(self, valor):
        if valor < 0:
            raise ValueError("El cupón de descuento debe ser 0 o positivo")
        self._cupon_descuento = valor

    def importeACobrar(self):
        importe = self.importe_medicamentos
        # Descuento por cupón
        if self.cupon_descuento > 0:
            importe -= self.cupon_descuento
        # Tipo de cobro
        if self.tipo_cobro == 2:
            importe *= 1.3  # Tarjeta de crédito: +30%
        elif self.tipo_cobro == 1:
            importe *= 0.95  # Efectivo: -5%
        return round(importe, 2)

    def __str__(self):
        return f"Farmacia(codigo={self.codigo}, tipo_cobro={self.tipo_cobro}, importe_medicamentos={self.importe_medicamentos}, cupon_descuento={self.cupon_descuento})"
