from Persona import *
from functools import reduce


def main():
    
    with open("./personas.csv", "r") as archivo:
        mayores = 0
        apellidosVocales = []
        diccionario = {}
        apellidos = {}
        for line in archivo:
   
            persona = line.split(",")
            persona = Persona(int(persona[0]), persona[1], persona[2], int(persona[3]))
            diccionario[persona.documento] = persona

            # métricas a calcular
            mayores += 1 if persona.es_mayor_de_edad() else 0
            if persona.es_vocal_apellido():
                apellidosVocales.append(persona.nombre + ' ' + persona.apellido)
            if persona.apellido in apellidos:
                apellidos[persona.apellido] += 1
            else:
                apellidos[persona.apellido] = 1
           
    
    print("RESULTADOS OMG!!")
    print("------------------")
    print("cantidad de personas cargadas: ", len(diccionario))
    print("cantidad de personas mayores de edad:", mayores)
    print("personas con apellido que comienza con vocal:", apellidosVocales)
    print("apellidos repetidos: ", apellidos)
    




if __name__ == "__main__":
    main()