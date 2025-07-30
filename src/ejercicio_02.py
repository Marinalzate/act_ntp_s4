def sistema_calificaciones():
    """
    Solicita al usuario ingresar calificaciones hasta escribir 'fin'.
    Luego muestra promedio, nota más alta y nota más baja.
    """
    calificaciones = []

    while True:
        entrada = input("Ingrese una calificación (o 'fin' para terminar): ")
        if entrada.lower() == 'fin':
            break
        try:
            nota = float(entrada)
            calificaciones.append(nota)
        except ValueError:
            print("Por favor, ingrese un número válido o 'fin'.")

    if len(calificaciones) == 0:
        print("No se ingresaron calificaciones.")
    else:
        promedio = sum(calificaciones) / len(calificaciones)
        nota_max = max(calificaciones)
        nota_min = min(calificaciones)

        print("\n📊 Resultados:")
        print(f"Promedio: {promedio:.2f}")
        print(f"Nota más alta: {nota_max}")
        print(f"Nota más baja: {nota_min}")

sistema_calificaciones()

