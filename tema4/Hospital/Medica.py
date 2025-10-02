from Atencion import Atencion

class Medica(Atencion):
    def __init__(self, codigo, tipo_cobro, paciente, importe_consulta):
        super().__init__(codigo, tipo_cobro)
        self._paciente = paciente
        self._importe_consulta = importe_consulta

    @property
    def paciente(self):
        return self._paciente

    @paciente.setter
    def paciente(self, valor):
        self._paciente = valor

    @property
    def importe_consulta(self):
        return self._importe_consulta

    @importe_consulta.setter
    def importe_consulta(self, valor):
        self._importe_consulta = valor

    def importeACobrar(self):
        importe = self.importe_consulta
        # Descuento por paciente habitual
        if hasattr(self.paciente, 'es_habitual') and self.paciente.es_habitual:
            importe *= 0.75  # 25% de descuento
        # Tipo de cobro
        if self.tipo_cobro == 2:
            importe *= 1.2  # Tarjeta de crédito: +20%
        elif self.tipo_cobro == 1:
            importe *= 0.9  # Efectivo: -10%
        return round(importe, 2)

    def __str__(self):
        return f"Medica(codigo={self.codigo}, tipo_cobro={self.tipo_cobro}, paciente={self.paciente}, importe_consulta={self.importe_consulta})"
