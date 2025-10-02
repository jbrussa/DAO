from hotel import Hotel
from habitacion import Habitacion
from estandar import Estandar
from suite import Suite
from suite_premium import SuitePremium

def main():
    with open("habitaciones.csv", "r") as archivo:
        hotel = Hotel("habitaciones.csv")
        
        print("2 - Suma de costo total de reservas:", hotel.obtener_suma_reservas())
        reserva_mas_cara = hotel.obtener_reserva_mas_cara()
        if reserva_mas_cara:
            print("3 - Reserva más cara:", reserva_mas_cara.numero, reserva_mas_cara.huesped, reserva_mas_cara.calcular_costo())
        print("4 - Ingreso total del hotel:", hotel.calcular_ingreso_total())
        print("5 - Cantidad de suites con vista al mar:", hotel.contar_suites_vista_mar())
        print("6 - Cantidad de suites premium con jacuzzi:", hotel.contar_suites_premium_jacuzzi())
        conteo = hotel.cantidad_por_tipo()
        print("7 - Cantidad de reservas por tipo de habitacion:", conteo)




if __name__ == "__main__":
    main()