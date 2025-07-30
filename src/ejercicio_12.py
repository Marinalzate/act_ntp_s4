def interseccion_conjuntos():
    """
    Muestra la interseccion entre dos conjuntos.
    """

    conjunto_a = {1, 2, 3, 4, 5}
    conjunto_b = {4, 5, 6, 7, 8}

    interseccion = conjunto_a & conjunto_b

    print("Elementos comunes entre los dos conjuntos:")
    print(interseccion)

interseccion_conjuntos()