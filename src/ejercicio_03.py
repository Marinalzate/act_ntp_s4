def combinar_listas(lista1, lista2):
    """
    Recibe dos listas del mismo tamaño y las combina elemento por elemento.
    Retorna una nueva lista intercalada.
    """
    if len(lista1) != len(lista2):
        return "Error: Las listas deben tener el mismo tamaño."
    
    combinada = []
    for i in range(len(lista1)):
        combinada.append(lista1[i])
        combinada.append(lista2[i])

    return combinada

lista_numeros = [1,2,3]
lista_letras = ['a', 'b', 'c']
resultado = combinar_listas(lista_numeros, lista_letras)
print("Lista combinada:", resultado)    