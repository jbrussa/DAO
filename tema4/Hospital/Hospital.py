from Atencion import Atencion

class Hospital:
    
    def __str__(self):
        atenciones_str = '\n'.join(str(a) for a in self._atenciones)
        return f"Hospital(razon_social={self._razon_social})\nAtenciones:\n{atenciones_str if atenciones_str else 'Sin atenciones'}"
    
    def __init__(self, razon_social):
        self._razon_social = razon_social
        self._atenciones = set()  # Colección (set) de objetos Atencion

    # Getter y setter para razon_social
    @property
    def razon_social(self):
        return self._razon_social

    @razon_social.setter
    def razon_social(self, valor):
        self._razon_social = valor

    # Getter y setter para atenciones
    @property
    def atenciones(self):
        return self._atenciones

    @atenciones.setter
    def atenciones(self, nuevas_atenciones):
        if isinstance(nuevas_atenciones, set):
            self._atenciones = nuevas_atenciones
        else:
            raise TypeError("Las atenciones deben ser un conjunto (set) de Atencion")

    def agregar_atencion(self, atencion):
        if isinstance(atencion, Atencion):
            self._atenciones.add(atencion)
        else:
            raise TypeError("La atención debe ser de tipo Atencion")

    def listar_atenciones(self):
        return list(self._atenciones)

    def importe_total_atencion_consulta(self):
        total = 0
        for atencion in self._atenciones:
            # Importa solo las atenciones médicas
            if atencion.__class__.__name__ == 'Medica':
                total += atencion.importe_consulta
        return total

    def importe_promedio_atenciones(self, valor_min, valor_max):
        print(f"Rango: {valor_min} - {valor_max}")
        todos_importes = []
        for a in self._atenciones:
            if a.__class__.__name__ == 'Medica':
                imp = a.importeACobrar()
                print(f"Medica codigo={a.codigo}, importeACobrar={imp}")
                todos_importes.append(imp)
        importes = [imp for imp in todos_importes if valor_min <= imp <= valor_max]
        print(f"Importes filtrados: {importes}")
        if importes:
            return round(sum(importes) / len(importes), 2)
        return 0

    def codigo_primera_atencion_habitual(self):
        for atencion in self._atenciones:
            if atencion.__class__.__name__ == 'Medica' and atencion.paciente.es_habitual:
                return atencion.codigo
        return 0