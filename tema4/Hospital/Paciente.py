class Paciente:
    def __init__(self, nombre, sintoma, es_habitual):
        self._nombre = nombre
        self._sintoma = sintoma  # 1: corazon, 2: pulmon, 3: otras
        self._es_habitual = es_habitual  # True o False

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def sintoma(self):
        return self._sintoma

    @sintoma.setter
    def sintoma(self, valor):
        self._sintoma = valor

    @property
    def es_habitual(self):
        return self._es_habitual

    @es_habitual.setter
    def es_habitual(self, valor):
        self._es_habitual = valor

    def __str__(self):
        sintomas = {1: "corazon", 2: "pulmon", 3: "otras"}
        return f"Paciente(nombre={self.nombre}, sintoma={sintomas.get(self.sintoma, self.sintoma)}, es_habitual={self.es_habitual})"
