def nombres_con_a():
    """
    Filtra e imprime los nombres que contienen la letra 'a'.
    """

    nombres = ("Ana", "Carlos", "Laura", "Juan", "Luis", "Sofia", "Pedro", "Maria")

    nombres_con_a = [nombre for nombre in nombres if 'a' in nombre.lower()]

    print("Nombres que contienen la letra 'a':")
    for nombre in nombres_con_a:
        print(nombre)

nombres_con_a()  