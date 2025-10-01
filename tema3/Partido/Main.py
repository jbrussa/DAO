from Partido import Partido
from Equipo import Equipo

if __name__ == "__main__":
    
    equipoA = Equipo("Equipo San Lorenzo")
    equipoB = Equipo("Equipo Belgrano")

    partido = Partido(equipoA, equipoB)

    print(" Inicio del partido")
    partido.sumarGolEquipoLocal()
    partido.sumarGolEquipoLocal()
    partido.sumarGolEquipoVisitante()

  
    print(partido)
    print("Fin del partido \n")

    equipoA.registrarPartido(partido)
    equipoB.registrarPartido(partido)

    partido = Partido(equipoA, equipoB, 2, 3)
    equipoA.registrarPartido(partido)
    equipoB.registrarPartido(partido)

    partido = Partido(equipoA, equipoB, 6, 3)
    equipoA.registrarPartido(partido)
    equipoB.registrarPartido(partido)

    partido = Partido(equipoA, equipoB, 5, 3)
    equipoA.registrarPartido(partido)
    equipoB.registrarPartido(partido)

    print(equipoA)
    print(equipoB)