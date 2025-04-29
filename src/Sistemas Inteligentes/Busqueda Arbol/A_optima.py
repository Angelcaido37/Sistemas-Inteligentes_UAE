import heapq

def a_estrella(grafo, inicio, objetivo, heuristica):
    """
    Implementación del algoritmo A*.
    :param grafo: Diccionario que representa el grafo (pesos de las aristas).
    :param inicio: Nodo inicial.
    :param objetivo: Nodo objetivo.
    :param heuristica: Función heurística que estima el costo desde un nodo al objetivo.
    :return: Lista con el camino óptimo o None si no hay camino.
    """
    # Cola de prioridad para almacenar nodos a explorar
    cola_prioridad = [] #Usamos heapq para implementar una cola de prioridad. Los nodos se insertan en la cola con su valor f(n), lo que permite extraer siempre el nodo con menor costo estimado.
    heapq.heappush(cola_prioridad, (0, inicio))  # (f(n), nodo)

    # Diccionario para almacenar el costo acumulado hasta cada nodo
    g = {nodo: float('inf') for nodo in grafo}
    g[inicio] = 0

    # Diccionario para reconstruir el camino
    padres = {inicio: None}

    while cola_prioridad:
        # Extraemos el nodo con menor f(n)
        costo_actual, nodo_actual = heapq.heappop(cola_prioridad)

        # Si llegamos al objetivo, reconstruimos el camino
        if nodo_actual == objetivo:
            camino = []
            while nodo_actual:
                camino.append(nodo_actual)
                nodo_actual = padres[nodo_actual]
            return camino[::-1]  # Invertimos el camino para que vaya del inicio al objetivo

        # Exploramos los vecinos del nodo actual
        for vecino, peso in grafo[nodo_actual].items():
            costo_tentativo = g[nodo_actual] + peso #Un diccionario g almacena el costo acumulado desde el nodo inicial hasta cada nodo. Inicialmente, todos los costos son infinitos excepto el nodo inicial.

            # Si encontramos un camino mejor hacia el vecino
            if costo_tentativo < g[vecino]:
                g[vecino] = costo_tentativo
                f_vecino = costo_tentativo + heuristica(vecino, objetivo)
                heapq.heappush(cola_prioridad, (f_vecino, vecino))
                padres[vecino] = nodo_actual #Un diccionario padres guarda el nodo padre de cada nodo visitado. Esto permite reconstruir el camino desde el objetivo hasta el inicio una vez encontrado.

    # Si no se encuentra un camino
    return None


# Ejemplo de uso
if __name__ == "__main__":
    # Grafo representado como un diccionario de adyacencia con pesos
    grafo = {
        'A': {'B': 1, 'C': 3},
        'B': {'A': 1, 'D': 2, 'E': 4},
        'C': {'A': 3, 'F': 2},
        'D': {'B': 2},
        'E': {'B': 4, 'F': 1},
        'F': {'C': 2, 'E': 1}
    }

    # Función heurística (distancia manhattan simplificada)
    def heuristica(nodo, objetivo): #La función heurística h(n) estima el costo restante desde un nodo al objetivo. En este ejemplo, usamos una heurística simple basada en la diferencia de caracteres ASCII.
        # En este ejemplo, usamos una heurística simple basada en la distancia entre letras
        return abs(ord(nodo) - ord(objetivo))

    # Parámetros del algoritmo
    inicio = 'A'
    objetivo = 'F'

    # Ejecutar A*
    camino = a_estrella(grafo, inicio, objetivo, heuristica)

    # Resultado
    if camino: #Si se llega al nodo objetivo, se reconstruye el camino usando el diccionario padres. Si no se encuentra un camino, se devuelve None.
        print(f"Camino óptimo de {inicio} a {objetivo}: {' -> '.join(camino)}")
    else:
        print(f"No hay camino de {inicio} a {objetivo}.")