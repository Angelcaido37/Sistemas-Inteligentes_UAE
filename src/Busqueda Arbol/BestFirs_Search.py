import heapq #Usamos heapq para implementar una cola de prioridad. Los nodos se insertan en la cola con su valor heurístico, lo que permite extraer siempre el nodo con menor valor heurístico.

def primero_el_mejor(inicio, objetivo, funcion_heuristica, generar_sucesores):
    """
    Implementación básica del algoritmo Primero el Mejor.
    :param inicio: Nodo inicial.
    :param objetivo: Estado objetivo a alcanzar.
    :param funcion_heuristica: Función que evalúa la calidad de un nodo.
    :param generar_sucesores: Función que genera los sucesores de un nodo dado.
    :return: Lista con el camino al objetivo o None si no se encuentra.
    """
    # Cola de prioridad para almacenar nodos a explorar
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (funcion_heuristica(inicio, objetivo), [inicio]))  # (heurística, camino)
#Un conjunto visitados asegura que no procesemos el mismo nodo más de una vez.
    visitados = set()  # Conjunto para llevar registro de nodos visitados

    while cola_prioridad:
        # Extraemos el nodo con menor valor heurístico
        _, camino = heapq.heappop(cola_prioridad)
        nodo_actual = camino[-1]

        # Si encontramos el objetivo, retornamos el camino
        if nodo_actual == objetivo:
            return camino

        # Marcar el nodo actual como visitado
        if nodo_actual in visitados:
            continue
        visitados.add(nodo_actual)

        # Generar los sucesores del nodo actual
        for sucesor in generar_sucesores(nodo_actual):
            if sucesor not in visitados:
                nuevo_camino = camino + [sucesor]
                heapq.heappush(cola_prioridad, (funcion_heuristica(sucesor, objetivo), nuevo_camino))

    # Si no se encuentra el objetivo
    return None


# Funciones auxiliares (ejemplo simplificado)
def generar_sucesores(nodo): #La función generar_sucesores devuelve los posibles estados siguientes para un nodo dado.
    """
    Genera los sucesores de un nodo dado.
    :param nodo: Nodo actual.
    :return: Lista de sucesores.
    """
    # Ejemplo simplificado: supongamos que los nodos son números y los sucesores son +1 y -1
    return [nodo + 1, nodo - 1]

def funcion_heuristica(nodo, objetivo): #La función funcion_heuristica estima qué tan cerca está un nodo del objetivo. En este ejemplo, usamos la distancia absoluta al objetivo.
    """
    Evalúa la calidad de un nodo usando una heurística.
    :param nodo: Nodo a evaluar.
    :param objetivo: Estado objetivo.
    :return: Valor de la heurística (cuanto menor, mejor).
    """
    # Ejemplo simplificado: queremos minimizar la distancia al objetivo
    return abs(objetivo - nodo)

# Ejemplo de uso
if __name__ == "__main__":
    inicio = 0  # Nodo inicial
    objetivo = 10  # Estado objetivo

    camino = primero_el_mejor(inicio, objetivo, funcion_heuristica, generar_sucesores)

    if camino:
        print(f"Camino encontrado: {camino}")
    else:
        print("No se encontró un camino.")