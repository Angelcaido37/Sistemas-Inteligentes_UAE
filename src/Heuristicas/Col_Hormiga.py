import random
import numpy as np

# Parámetros del algoritmo
NUM_CIUDADES = 5          # Número de ciudades
NUM_HORMIGAS = 10         # Número de hormigas
NUM_ITERACIONES = 50      # Número de iteraciones
ALPHA = 1                 # Importancia de las feromonas
BETA = 2                  # Importancia de la distancia
EVAPORACION = 0.5         # Tasa de evaporación de feromonas
Q = 100                   # Constante para la deposición de feromonas

# Matriz de distancias entre ciudades
distancias = [
    [0, 290, 490, 700, 900],  # Distancias desde la ciudad de Tepic a Ensenada
    [290, 20, 35, 25, 30],  # Distancias desde la ciudad 1
    [15, 35, 0, 30, 20],  # Distancias desde la ciudad 2
    [20, 25, 30, 0, 15],  # Distancias desde la ciudad 3
    [25, 30, 20, 15, 0]   # Distancias desde la ciudad 4
]

# Inicializar feromonas
feromonas = [[1 for _ in range(NUM_CIUDADES)] for _ in range(NUM_CIUDADES)]

# Función para calcular la probabilidad de elegir una ciudad
def calcular_probabilidades(ciudad_actual, ciudades_no_visitadas):
    probabilidades = []
    total = 0
    for ciudad in ciudades_no_visitadas:
        tau = feromonas[ciudad_actual][ciudad]  # Feromonas en el camino
        eta = 1 / distancias[ciudad_actual][ciudad]  # Atractivo basado en la distancia
        prob = (tau ** ALPHA) * (eta ** BETA)
        probabilidades.append(prob)
        total += prob
    return [p / total for p in probabilidades]  # Normalizar probabilidades

# Construir una ruta para una hormiga
def construir_ruta():
    ruta = []
    ciudades_no_visitadas = list(range(NUM_CIUDADES))
    ciudad_actual = random.choice(ciudades_no_visitadas)  # Elegir una ciudad inicial al azar
    ruta.append(ciudad_actual)
    ciudades_no_visitadas.remove(ciudad_actual)

    while ciudades_no_visitadas:
        probabilidades = calcular_probabilidades(ciudad_actual, ciudades_no_visitadas)
        siguiente_ciudad = random.choices(ciudades_no_visitadas, weights=probabilidades)[0]
        ruta.append(siguiente_ciudad)
        ciudades_no_visitadas.remove(siguiente_ciudad)
        ciudad_actual = siguiente_ciudad

    return ruta

# Calcular la longitud total de una ruta
def calcular_longitud_ruta(ruta):
    longitud = 0
    for i in range(len(ruta)):
        ciudad_actual = ruta[i]
        ciudad_siguiente = ruta[(i + 1) % len(ruta)]
        longitud += distancias[ciudad_actual][ciudad_siguiente]
    return longitud

# Actualizar feromonas
def actualizar_feromonas(rutas, longitudes):
    global feromonas
    # Evaporación de feromonas
    feromonas = [[feromona * (1 - EVAPORACION) for feromona in fila] for fila in feromonas]

    # Depositar feromonas en las rutas
    for ruta, longitud in zip(rutas, longitudes):
        delta_feromona = Q / longitud
        for i in range(len(ruta)):
            ciudad_actual = ruta[i]
            ciudad_siguiente = ruta[(i + 1) % len(ruta)]
            feromonas[ciudad_actual][ciudad_siguiente] += delta_feromona
            feromonas[ciudad_siguiente][ciudad_actual] += delta_feromona

# Algoritmo de Colonia de Hormigas
def algoritmo_colonia_hormigas():
    mejor_ruta_global = None
    mejor_longitud_global = float('inf')

    for iteracion in range(NUM_ITERACIONES):
        rutas = []
        longitudes = []

        # Construir rutas para todas las hormigas
        for _ in range(NUM_HORMIGAS):
            ruta = construir_ruta()
            longitud = calcular_longitud_ruta(ruta)
            rutas.append(ruta)
            longitudes.append(longitud)

            # Actualizar la mejor ruta global
            if longitud < mejor_longitud_global:
                mejor_longitud_global = longitud
                mejor_ruta_global = ruta

        # Actualizar feromonas
        actualizar_feromonas(rutas, longitudes)

        print(f"Iteración {iteracion}: Mejor ruta = {mejor_ruta_global}, Longitud = {mejor_longitud_global}")

    return mejor_ruta_global, mejor_longitud_global

# Ejecutar el algoritmo
if __name__ == "__main__":
    mejor_ruta, mejor_longitud = algoritmo_colonia_hormigas()
    print(f"\nMejor ruta encontrada: {mejor_ruta}, Longitud = {mejor_longitud}")