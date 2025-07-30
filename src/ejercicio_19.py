def mayores_de_edad():
    """
    Imprime los nombres de las personas mayores de edad (18+)
    """

    edades = {
        "Ana": 17,
        "Carlos": 22,
        "Laura": 19,
        "Juan": 16,
        "Sofia": 25,
        "Luis": 18
    }

    print("Perssonas mayores de edad:")
    for nombre, edad in edades.items():
        if edad >= 18:
            print(nombre)

mayores_de_edad()            