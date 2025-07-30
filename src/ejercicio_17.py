def mejor_estudiante():
    """
    Encuentra e imprime el nombre del estudiante con la nota mas alta.
    """
    notas = {
        "Ana": 4.5,
        "Carlos": 3.8,
        "Laura": 4.9,
        "Juan": 4.2,
        "Sofia": 4.7
    }

    mejor = max(notas, key=notas.get)
    print(f"El estudiante con la nota mas alta es: {mejor} con {notas[mejor]}")

mejor_estudiante()    