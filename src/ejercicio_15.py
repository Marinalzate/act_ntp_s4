def mayores_de_25():
    """
    Imprime los nombres de las personas con edad mayor a 25.
    """

    personas = {
        "Ana": 25,
        "Carlos": 30,
        "Laura": 22,
        "Juan": 28,
        "Sofia": 26
    }

    print("Personas mayores de 25 años:")
    for nombre, edad in personas.items():
        if edad > 25:
            print(nombre)

mayores_de_25()       