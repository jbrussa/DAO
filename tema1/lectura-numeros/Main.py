def promedio (numeros: list) -> float:
    if not numeros:
        return 0
    return sum(int(num.strip()) for num in numeros) / len(numeros)

def main():
    mayores_al_promedio = 0

    try:
        with open("numeros.txt", "r") as file:
            numeros = file.readlines()
        
        promedio_numeros = promedio(numeros)
        print(f"El promedio de los números es: {promedio_numeros:.2f}")

        for i in range(len(numeros)):
            numero = int(numeros[i].strip())
            if numero > promedio_numeros:
                mayores_al_promedio += 1
        
        pares = filter(lambda x: pares(int(x.strip())), numeros)

    except FileNotFoundError:
        print("El archivo 'numeros.txt' no se encontró.")
    except ValueError:
        print("Asegúrate de que el archivo contenga solo números enteros.")



if __name__ == "__main__":
    main()