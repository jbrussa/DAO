from biblioteca import Biblioteca


def main():
    csv_path = "material.csv"
    biblioteca = Biblioteca(csv_path)

    print("--- Resumen Biblioteca ---")
    print("2 - Promedio entero de precios base", biblioteca.calcular_promedio_precios_base())
    print("3 - Material con mayor costo de mantenimiento:", biblioteca.obtener_material_mayor_costo_mantenimiento().titulo)
    print("4 - Suma de costos de mantenimiento:", biblioteca.calcular_suma_costo_mantenimiento())
    print("5 - Cantidad de libros prestados más de 30 días:", biblioteca.contar_libros_mas_30_dias())
    print("6 - Cantidad de revistas importadas:", biblioteca.contar_revistas_importadas())
    print("7 - Cantidad de materiales por tipo:", biblioteca.cantidad_por_tipo())

if __name__ == "__main__":
    main()
