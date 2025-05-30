import random
import math

# pitagoras
def distancia_origen(x, y):
    return math.sqrt(x**2 + y**2)

# algoritmo divide y vencerás
def coordenada_mas_alejada(coordenadas):
    if len(coordenadas) == 0:
        return None
    if len(coordenadas) == 1:
        x, y = coordenadas[0]
        if x > 0 and y < 0:
            return coordenadas[0]
        else:
            return None
    
    medio = len(coordenadas) // 2
    izquierda = coordenada_mas_alejada(coordenadas[:medio])
    derecha = coordenada_mas_alejada(coordenadas[medio:])

    def obtener_distancia(coord):
        if coord is None:
            return -1
        return distancia_origen(coord[0], coord[1])

    if obtener_distancia(izquierda) > obtener_distancia(derecha):
        return izquierda
    else:
        return derecha

n = int(input("Ingresa la cantidad de pares de coordenadas: "))
#generamos la matriz de coordenadas aleatorias
matriz = [[random.randint(-81, 81), random.randint(-81, 81)] for _ in range(n)]

# Muestra las coordenadas generadas
print("\nCoordenadas generadas:")
for coord in matriz:
    print(coord)

# para encontrar la coordenada más alejada del (0,0) que cumpla con X > 0 e Y < 0
resultado = coordenada_mas_alejada(matriz)

if resultado:
    print(f"\ncoordenada más alejada del (0,0) con X > 0 e Y < 0: {resultado}")
    print(f"distancia: {distancia_origen(resultado[0], resultado[1]):.2f}")
else:
    print("\nno hay coordenadas con X > 0 e Y < 0.")


