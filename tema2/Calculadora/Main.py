

def ejecutar_calculadora():
    
    suma = lambda a, b: a + b
    resta = lambda a, b: a - b
    multiplicacion = lambda a, b: a * b
    division = lambda a, b: a / b
    operaciones = [None, suma, resta, multiplicacion, division]

    print("Calculadora básica")
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("0. Salir")

    opcion = int(input())

    while opcion != 0:
        if opcion >= 1 and opcion <= 4:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            
            resultado = operaciones[opcion](a, b)
            print("El resultado es:", resultado)
        else:
            print("Opción inválida. Intente nuevamente.")
        
        print()
        print("Seleccione una operación:")
        opcion = int(input())

ejecutar_calculadora()