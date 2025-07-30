import random
import math

def generar_coordenadas():
    """
    Genera una tupla de 10 coordenadas (x, y) aleatorias entre -10 y 10,
    y muestra las que están dentro de un círculo de radio 5 centrado en el origen.
    """
    puntos = tuple((random.randint(-10, 10), random.randint(-10, 10)) for _ in range(10))
    
    print("📍 Coordenadas generadas:")
    for punto in puntos:
        print(punto)

    dentro_circulo = []

    for x, y in puntos:
        distancia = math.sqrt(x**2 + y**2)
        if distancia <= 5:
            dentro_circulo.append((x, y))

    print("\n🟢 Puntos dentro del círculo de radio 5:")
    for p in dentro_circulo:
        print(p)

generar_coordenadas()
