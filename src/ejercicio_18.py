def total_compra():
    """
    Calcula el precio total de comprar uno de cada producto.
    """

    productos = {
        "Pan": 2500,
        "Leche": 3200,
        "Queso": 5500,
        "Huevos": 4000,
        "Cafe": 8000
    }

    total = sum(productos.values())
    print(f"Total a pagar por uno de cada producto: ${total}")

total_compra() 