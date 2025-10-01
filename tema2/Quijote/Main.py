
def Main():
    
    with open("quijote.txt", "r", encoding="utf-8") as file:
        texto = file.read()
        """Obtener palabras únicas del libro"""
        palabras_libro = set(texto.split())


    with open("words_alpha.txt", "r", encoding="utf-8") as diccionario:
        palabras_diccionario = set(diccionario.read().splitlines())

    """ Resultados """
    print(f"Cantidad de palabras únicas en el libro: {len(palabras_libro)}")
    print(f"Cantidad de palabras del diccionario: {len(palabras_diccionario)}")
    print(f"Cantidad de palabras del libro que no existen en el diccionario: {len(palabras_diccionario)}")

    palabras_no_en_diccionario = palabras_libro - palabras_diccionario
    palabras_no_en_diccionario_ordenadas = sorted(palabras_no_en_diccionario)
    print("Listado de palabras que no existen en el diccionario:")
    for palabra in palabras_no_en_diccionario_ordenadas:
        print(palabra)


if __name__ == "__main__":
    Main()






