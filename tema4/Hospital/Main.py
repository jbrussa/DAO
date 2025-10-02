from Hospital import Hospital
from Medica import Medica
from Paciente import Paciente


def main():
    # Crear hospital
    hospital = Hospital("Hospital Central")

    # Crear pacientes
    pacientes = [
        Paciente("Juan", 1, True),
        Paciente("Ana", 2, False),
        Paciente("Luis", 3, True),
        Paciente("Marta", 1, False),
        Paciente("Pedro", 2, True)
    ]

    # Crear atenciones médicas
    medicas = [
        Medica(101, 1, pacientes[0], 1000),
        Medica(102, 2, pacientes[1], 1000),
        Medica(103, 1, pacientes[2], 900),
        Medica(104, 2, pacientes[3], 1100),
        Medica(105, 1, pacientes[4], 950)
    ]

    # Crear atenciones de farmacia
    from Farmacia import Farmacia
    farmacias = [
        Farmacia(201, 1, 500, 50),
        Farmacia(202, 2, 700, 0),
        Farmacia(203, 1, 650, 20),
        Farmacia(204, 2, 800, 100),
        Farmacia(205, 1, 400, 0)
    ]

    # Agregar todas las atenciones al hospital
    for m in medicas:
        hospital.agregar_atencion(m)
    for f in farmacias:
        hospital.agregar_atencion(f)

    # Probar métodos del enunciado
    print(hospital)
    print("\nImporte total de consultas médicas:", hospital.importe_total_atencion_consulta())
    print("Importe promedio de atenciones médicas entre 800 y 1200:", hospital.importe_promedio_atenciones(800, 1200))
    print("Código de la primera atención médica de paciente habitual:", hospital.codigo_primera_atencion_habitual())






if __name__ == "__main__":
    main()