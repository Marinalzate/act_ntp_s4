def estudiantes_destacados():
    """
    Muestra los estudiantes cuyo promedio es mayor o igual a 3.5.
    """
    estudiantes = [
        ("Ana", 4.0),
        ("Carlos", 3.2),
        ("Laura", 3.9),
        ("Juan", 2.8),
        ("Sofía", 3.6)
    ]

    print("🎓 Estudiantes con promedio mayor o igual a 3.5:")
    for nombre, promedio in estudiantes:
        if promedio >= 3.5:
            print(f"{nombre}: {promedio}")

estudiantes_destacados()
   