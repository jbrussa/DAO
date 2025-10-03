class Ascensor:
    def __init__(self, piso_min: int, piso_max: int, capacidad: int):
        # validaciones básicas
        if piso_min > piso_max:
            raise ValueError("Rango de pisos inválido: piso_min > piso_max")
        if capacidad <= 0:
            raise ValueError("Capacidad debe ser mayor que 0")

        # según los tests, el edificio debe incluir el piso 0 en su rango
        if not (piso_min <= 0 <= piso_max):
            raise ValueError("El rango de pisos debe contener el piso 0")

        self._piso_min = int(piso_min)
        self._piso_max = int(piso_max)
        self._capacidad = int(capacidad)

        # estado inicial
        self._piso_actual = 0
        self._personas = 0

    @property
    def piso_actual(self) -> int:
        return self._piso_actual

    @property
    def personas(self) -> int:
        return self._personas

    def ir_a_piso(self, piso: int) -> bool:
        """Mueve el ascensor al piso indicado si está dentro del rango.

        Retorna True si el movimiento fue exitoso y False si el piso está fuera de rango.
        No cambia el piso actual si la solicitud es inválida.
        """
        try:
            piso = int(piso)
        except Exception:
            return False

        if self._piso_min <= piso <= self._piso_max:
            self._piso_actual = piso
            return True
        return False

    def subir(self, cantidad: int) -> int:
        """Intenta subir `cantidad` personas al ascensor.

        - Si cantidad <= 0 retorna -1 (invalido).
        - Si hay espacio suficiente retorna el número que sube (y lo suma a personas).
        - Si no hay espacio, suben las que entran (hasta capacidad) y se retorna ese número.
        """
        try:
            cantidad = int(cantidad)
        except Exception:
            return -1

        if cantidad <= 0:
            return -1

        espacio = self._capacidad - self._personas
        if espacio <= 0:
            return 0

        a_subir = cantidad if cantidad <= espacio else espacio
        self._personas += a_subir
        return a_subir

    def bajar(self, cantidad: int) -> int:
        """Intenta bajar `cantidad` personas del ascensor.

        - Si cantidad <= 0 retorna -1 (invalido).
        - Si hay menos personas que cantidad, bajan todas las personas y se retorna el número bajado.
        """
        try:
            cantidad = int(cantidad)
        except Exception:
            return -1

        if cantidad <= 0:
            return -1

        if cantidad >= self._personas:
            bajan = self._personas
            self._personas = 0
            return bajan

        # cantidad < personas
        self._personas -= cantidad
        return cantidad
