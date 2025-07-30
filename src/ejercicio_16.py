def calcular_total_compra():
    """
    Calcula el precio total de una compra basada en una lista de productos.
    """

    productos = {
        "manzana": 0.5,
        "pan": 1.0,
        "leche": 1.5,
        "huevos": 2.0,
        "arroz": 1.2
    }

    carrito = ["pan", "leche", "arroz"]

    total = 0
    for producto in carrito:
        if producto in producto:
            total += productos[producto]

    print(f"Total de la compra: ${total:.2f}")    

calcular_total_compra()        