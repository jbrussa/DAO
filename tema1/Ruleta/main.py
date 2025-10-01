import random

RED = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
BLACK = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]

def tirar():
    return random.randint(0, 36)


def main():    
    print("Bienvenido a la ruleta")

    cero = 0
    par = 0
    impar = 0
    primeraDocena = 0
    segundaDocena = 0
    terceraDocena = 0
    red = 0
    black = 0

    for i in range(1000):
        numero = tirar()
        if numero == 0:
            cero +=1
        if numero % 2 == 0:
            par += 1
        if numero % 2 == 1:
            impar += 1
        if numero >= 1 and numero <= 12:
            primeraDocena += 1
        if numero >= 13 and numero <= 24:
            segundaDocena += 1
        if numero >= 25 and numero <= 36:
            terceraDocena += 1
        if numero in RED:
            red += 1
        if numero in BLACK:
            black += 1
    
    porcentaje = cero * 100 / 1000

    print("Resultados de la ruleta:")
    print(f"El porcentaje de veces que salió el cero es: {porcentaje}%")
    print(f"Par: {par}")
    print(f"Impar: {impar}")
    print(f"Primera docena: {primeraDocena}")
    print(f"Segunda docena: {segundaDocena}")
    print(f"Tercera docena: {terceraDocena}")
    print(f"Rojo: {red}")
    print(f"Black : {black}")

main()