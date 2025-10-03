# Curso: 4k2 
# Nombre: Julieta Brussa Osella
# Legajo: 95134

import csv
from typing import List, Dict, Optional
from material import Material
from libro import Libro
from ebook import Ebook
from revista import Revista


class Biblioteca:
    def __init__(self, csv_path: str):
        self.materiales: List[Material] = []
        try:
            with open(csv_path, "r", encoding='utf-8') as archivo:
                for line in archivo:
                    material = line.strip().split(",")
                    if not line:
                        continue
                    
                    tipo = int(material[0])
                    codigo = material[1]
                    titulo = material[2]
                    autor = material[3]
                    precio_base = float(material[4])
                    extra = material[5]
                    
                    if tipo == 1:
                        self.materiales.append(Libro(codigo, titulo, autor, float(precio_base), int(extra)))
                    elif tipo == 2:
                        self.materiales.append(Ebook(codigo, titulo, autor, float(precio_base), float(extra)))
                    elif tipo == 3:
                        self.materiales.append(Revista(codigo, titulo, autor, float(precio_base), extra))
                    else:
                        continue
        except FileNotFoundError:
            raise FileNotFoundError(csv_path)

    def cantidad_materiales(self) -> List[Material]:
        return self.materiales

    def cantidad_por_tipo(self) -> Dict[str, int]:
        conteo = {"Libro": 0, "Ebook": 0, "Revista": 0}
        for m in self.materiales:
            if isinstance(m, Libro):
                conteo["Libro"] += 1
            elif isinstance(m, Ebook):
                conteo["Ebook"] += 1
            elif isinstance(m, Revista):
                conteo["Revista"] += 1
        return conteo

    def calcular_promedio_precios_base(self) -> float:
        if not self.materiales:
            return 0
        total = sum(m.precio_base for m in self.materiales)
        return int(total / len(self.materiales))

    def obtener_material_mayor_costo_mantenimiento(self) -> Optional[Material]:
        if not self.materiales:
            return None
        return max(self.materiales, key=lambda m: m.calcular_costo_mantenimiento())

    def calcular_suma_costo_mantenimiento(self) -> float:
        return sum(m.calcular_costo_mantenimiento() for m in self.materiales)

    def contar_libros_mas_30_dias(self) -> int:
        return sum(1 for m in self.materiales if isinstance(m, Libro) and m.dias_prestados > 30)

    def contar_revistas_importadas(self) -> int:
        return sum(1 for m in self.materiales if isinstance(m, Revista) and m.origen == 'importada')

