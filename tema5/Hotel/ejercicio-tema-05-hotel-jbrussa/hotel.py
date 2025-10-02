
from estandar import Estandar
from suite import Suite
from suite_premium import SuitePremium
from habitacion import Habitacion
import csv
from typing import List, Optional


class Hotel:
	def __init__(self, csv_path: str):
		# Cargar habitaciones desde archivo
		self.habitaciones: List[Habitacion] = []
		try:
			with open(csv_path, newline='', encoding='utf-8') as csvfile:
				reader = csv.reader(csvfile)
				for row in reader:
					if not row:
						continue
					try:
						tipo = int(row[0])
						numero = int(row[1])
						huesped = row[2]
						costo_base = float(row[3])
						noches = int(row[4])
						extra = row[5].strip().lower() in ('true', '1', 'si', 's', 'yes')
					except Exception:
						raise ValueError("Archivo con formato inválido")

					if tipo == 1:
						self.habitaciones.append(Estandar(numero, huesped, costo_base, noches, extra))
					elif tipo == 2:
						self.habitaciones.append(Suite(numero, huesped, costo_base, noches, extra))
					elif tipo == 3:
						self.habitaciones.append(SuitePremium(numero, huesped, costo_base, noches, extra))
					else:
						continue
		except FileNotFoundError:
			raise FileNotFoundError(csv_path)

	def cantidad_habitaciones(self) -> int:
		return len(self.habitaciones)

	def cantidad_por_tipo(self):
		conteo = {"Estandar": 0, "Suite": 0, "SuitePremium": 0}
		for h in self.habitaciones:
			if isinstance(h, Estandar):
				conteo["Estandar"] += 1
			elif isinstance(h, Suite):
				conteo["Suite"] += 1
			elif isinstance(h, SuitePremium):
				conteo["SuitePremium"] += 1
		return conteo

	def obtener_suma_reservas(self) -> float:
		return sum(h.calcular_costo() for h in self.habitaciones)

	def obtener_reserva_mas_cara(self) -> Optional[Habitacion]:
		if not self.habitaciones:
			return None
		return max(self.habitaciones, key=lambda h: h.calcular_costo())

	def calcular_ingreso_total(self) -> float:
		# igual a obtener_suma_reservas en este ejercicio
		return self.obtener_suma_reservas()

	def contar_suites_vista_mar(self) -> int:
		return sum(1 for h in self.habitaciones if isinstance(h, Suite) and h.vista_mar)

	def contar_suites_premium_jacuzzi(self) -> int:
		return sum(1 for h in self.habitaciones if isinstance(h, SuitePremium) and h.jacuzzi)


