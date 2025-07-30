def filtrar_pares(lista):
    """
    Recibe una lista de numeros y devuelve una lista con solo numeros pares.
    """
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return pares


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = filtrar_pares(numeros)
print("Numeros pares:", resultado)