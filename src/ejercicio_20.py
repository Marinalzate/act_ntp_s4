def promedios_estudiantes():
    """
    Calcula e imprime el promedio de notas de cada estudiante.
    """

    estudiantes = {
        "Ana": [3.5, 4.0, 4.2],
        "Carlos": [2.8, 3.1, 3.9],
        "Laura": [4.5, 4.6, 4.9],
        "Juan": [3.0, 2.9, 3.4]
    }

    print("Promedios de los estudiantes:")
    for nombre, notas in estudiantes.items():
        promedio = sum(notas) / len(notas)
        print(f"{nombre}: {promedio:.2f}")

promedios_estudiantes()        