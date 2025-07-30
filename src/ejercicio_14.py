def imprimir_edad_personas():
    """
    Imprime el nombre y la edad de varias personas usando el diccionario.
    """
    personas = {
        "Ana": 25,
        "Carlos": 30,
        "Laura": 22,
        "Juan": 28,
        "Sofia": 26
    }

    print("Listado de edades:")
    for nombre, edad in personas.items():
        print(f"{nombre}: {edad} años")

imprimir_edad_personas()   