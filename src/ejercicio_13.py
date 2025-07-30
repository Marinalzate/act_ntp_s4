def eliminar_fruta():
    """
    Elimina 'banana' del conjunto de frutas si esta presente.
    """
    frutas = {"manza", "banana", "pera", "naranja", "uva"}

    frutas.discard("banana")

    print("Conjunto de frutas despues de eliminar 'banana':")
    print(frutas)

eliminar_fruta()