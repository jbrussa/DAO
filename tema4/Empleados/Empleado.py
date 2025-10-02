
from __future__ import annotations
from typing import List, Optional
import os
from abc import ABC, abstractmethod

class Empleado:
    def __init__(self, legajo: int, nombre: str, apellido: str, sueldo_basico: float):
        self.legajo = int(legajo)
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo_basico = float(sueldo_basico)

    @abstractmethod
    def sueldo_a_cobrar(self) -> float:
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(legajo={self.legajo}, nombre={self.nombre}, apellido={self.apellido}, sueldo_basico={self.sueldo_basico})"


class Obrero(Empleado):
    def __init__(self, legajo: int, nombre: str, apellido: str, sueldo_basico: float, dias_trabajados: int):
        super().__init__(legajo, nombre, apellido, sueldo_basico)
        self.dias_trabajados = int(dias_trabajados)

    def sueldo_a_cobrar(self) -> float:
        return (self.sueldo_basico / 20.0) * self.dias_trabajados


class Administrativo(Empleado):
    def __init__(self, legajo: int, nombre: str, apellido: str, sueldo_basico: float, presentismo: bool):
        super().__init__(legajo, nombre, apellido, sueldo_basico)
        self.presentismo = bool(presentismo)

    def sueldo_a_cobrar(self) -> float:
        return self.sueldo_basico * (1.13 if self.presentismo else 1.0)


class Vendedor(Empleado):
    def __init__(self, legajo: int, nombre: str, apellido: str, sueldo_basico: float, ventas_totales: float):
        super().__init__(legajo, nombre, apellido, sueldo_basico)
        self.ventas_totales = float(ventas_totales)

    def sueldo_a_cobrar(self) -> float:
        return self.sueldo_basico + 0.01 * self.ventas_totales
