def buscar_palabras_con_letra(lista_palabras):
    """
    Pide una letra al usuario y devuelve una lista con las palabras que la contienen.
    """
    letra = input("🔡 Ingresa la letra a buscar: ").lower()
    resultado = []

    for palabra in lista_palabras:
        for caracter in palabra:
            if caracter.lower() == letra:
                resultado.append(palabra)
                break  # Evita agregar la misma palabra varias veces

    return resultado

# Prueba de la función
palabras = ["python", "java", "kotlin", "javascript", "html", "css", "sql"]
encontradas = buscar_palabras_con_letra(palabras)
print("🔍 Palabras que contienen la letra:", encontradas)
