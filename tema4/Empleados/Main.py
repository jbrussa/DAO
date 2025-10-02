from Empleado import Empleado, Obrero, Administrativo, Vendedor

def main():
    with open("./empleados.csv", "r") as archivo:
        cantidad_obreros = 0
        cantidad_administrativos = 0
        cantidad_vendedores = 0
        total_sueldos = 0.0

        for line in archivo:
            parts = [p.strip() for p in line.split(";")]
            if len(parts) < 6:
                # línea inválida: saltar
                continue

            tipo = int(parts[0])
            legajo = int(parts[1])
            nombre = parts[2]
            apellido = parts[3]
            sueldo_basico = float(parts[4])
            campo = parts[5]

            if tipo == 1:
                # Obrero: campo -> días trabajados
                empleado = Obrero(legajo, nombre, apellido, sueldo_basico, int(campo))
                cantidad_obreros += 1
                total_sueldos += empleado.sueldo_a_cobrar()
            elif tipo == 2:
                # Administrativo: campo -> presentismo (booleano)
                presentismo = str(campo).strip().lower() in ("true", "1", "si", "s", "yes")
                empleado = Administrativo(legajo, nombre, apellido, sueldo_basico, presentismo)
                cantidad_administrativos += 1
                total_sueldos += empleado.sueldo_a_cobrar()
            elif tipo == 3:
                # Vendedor: campo -> total de ventas
                empleado = Vendedor(legajo, nombre, apellido, sueldo_basico, float(campo))
                cantidad_vendedores += 1
                total_sueldos += empleado.sueldo_a_cobrar()
            else:
                empleado = None

    print("Resumen de Empleados:")
    print(f"Cantidad de Obreros: {cantidad_obreros}")
    print(f"Cantidad de Administrativos: {cantidad_administrativos}")
    print(f"Cantidad de Vendedores: {cantidad_vendedores}")
    print(f"Sueldos totales a pagar: {total_sueldos:.2f}")

    with open("./empleados.csv", "r") as archivo:
        legajo_buscar = 1
        while legajo_buscar != 0:
            legajo_buscar = int(input("Ingrese el legajo del empleado a buscar, o 0 si no quiere buscar un empleado:   "))
            if legajo_buscar != 0:
                for line in archivo:
                    parts = [p.strip() for p in line.split(";")]
                
                    tipo = int(parts[0])
                    legajo = int(parts[1])
                    nombre = parts[2]
                    apellido = parts[3]
                    sueldo_basico = float(parts[4])
                    campo = parts[5]

                    print(f"Buscando legajo: {legajo_buscar}, Leyendo legajo: {legajo}")
                    if legajo_buscar == legajo:
                        if tipo == 1:
                            empleado = Obrero(legajo, nombre, apellido, sueldo_basico, int(campo))
                        elif tipo == 2:
                            presentismo = str(campo).strip().lower() in ("true", "1", "si", "s", "yes")
                            empleado = Administrativo(legajo, nombre, apellido, sueldo_basico, presentismo)
                        elif tipo == 3:
                            empleado = Vendedor(legajo, nombre, apellido, sueldo_basico, float(campo))
                        else:
                            empleado = None

                        print(f"Empleado encontrado: {empleado.nombre} {empleado.apellido}, Legajo: {empleado.legajo}, Sueldo a cobrar: {empleado.sueldo_a_cobrar():.2f}")
                        break
                else:
                    print("Empleado no encontrado.")
            else:
                print("Muchas gracias!")

            



           



if __name__ == "__main__":
    main()