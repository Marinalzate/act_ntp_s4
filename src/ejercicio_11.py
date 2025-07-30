def conjunto_sin_duplicados():
    """
    Muestra un conjunto sin duplicados y su longitud.
    """

    numeros = [1, 2, 3, 4, 5, 6, 7, 1]

    conjunto = set(numeros)

    print("Conjunto sin duplicados:")
    print(conjunto)
    print(f"Cantidad de elementos unicos: {len(conjunto)}")

conjunto_sin_duplicados() 