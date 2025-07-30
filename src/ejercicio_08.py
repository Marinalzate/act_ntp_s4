def contar_colores():
    """
    Cuenta cuántas veces aparece cada color favorito entre un grupo de personas.
    """
    preferencias = [
        ("Ana", "azul"),
        ("Carlos", "rojo"),
        ("Laura", "azul"),
        ("Juan", "verde"),
        ("Sofía", "rojo"),
        ("María", "azul"),
        ("Pedro", "verde"),
        ("Luis", "rojo"),
    ]

    conteo_colores = {}

    for _, color in preferencias:
        if color in conteo_colores:
            conteo_colores[color] += 1
        else:
            conteo_colores[color] = 1

    print("Recuento de colores favoritos:")
    for color, cantidad in conteo_colores.items():
        print(f"{color}: {cantidad}")  

contar_colores()
              