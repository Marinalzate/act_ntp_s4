def tupla_sin_duplicados():
    """
    Elimina duplicados de una tupla de nombres.
    """
    nombres = ("Ana", "Carlos", "Ana", "Laura", "Carlos", "Juan", "Laura", "Luis")

    nombres_unicos = tuple(set(nombres))

    print("Tupla original:")
    print(nombres)
    print("\nTupla sin duplicados:")
    print(nombres_unicos)

tupla_sin_duplicados()