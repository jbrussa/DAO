from ascensor import Ascensor


def demo():
    a = Ascensor(-2, 10, 5)
    print("Piso actual:", a.piso_actual)
    print("Ir a piso 3 ->", a.ir_a_piso(3))
    print("Piso actual:", a.piso_actual)
    print("Subir 3 personas ->", a.subir(3))
    print("Personas ahora:", a.personas)
    print("Bajar 2 personas ->", a.bajar(2))
    print("Personas ahora:", a.personas)


if __name__ == '__main__':
    demo()
