# Algoritmo DFS - Versión Iterativa

# Definimos el grafo como un diccionario de listas
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Algoritmo DFS - Versión Iterativa
def dfs_iterativo(grafo, inicio):
    """
    Función iterativa para realizar DFS.
    :param grafo: Diccionario que representa el grafo (lista de adyacencia).
    :param inicio: Nodo inicial desde donde comenzar el recorrido.
    """
    visitados = set()  # Conjunto para llevar registro de nodos visitados
    pila = [inicio]    # Pila para simular la recursión

    while pila:
        nodo = pila.pop()  # Extraemos el último nodo agregado a la pila
        if nodo not in visitados:
            visitados.add(nodo)
            print(nodo, end=" ")  # Imprimimos el nodo visitado

            # Agregamos los vecinos no visitados a la pila
            # IMPORTANTE: Se invierte el orden para mantener consistencia con la recursiva
            for vecino in reversed(grafo[nodo]):
                if vecino not in visitados:
                    pila.append(vecino)

def dfs_iterativo(grafo, inicio):
    """
    Función iterativa para realizar DFS.
    :param grafo: Diccionario que representa el grafo (lista de adyacencia).
    :param inicio: Nodo inicial desde donde comenzar el recorrido.
    """
    visitados = set()  # Conjunto para llevar registro de nodos visitados
    pila = [inicio]    # Pila para simular la recursión

    while pila:
        nodo = pila.pop()  # Extraemos el último nodo agregado a la pila
        if nodo not in visitados:
            visitados.add(nodo)
            print(nodo, end=" ")  # Imprimimos el nodo visitado

            # Agregamos los vecinos no visitados a la pila
            # IMPORTANTE: Se invierte el orden para mantener consistencia con la recursiva
            for vecino in reversed(grafo[nodo]):
                if vecino not in visitados:
                    pila.append(vecino)

# Ejemplo de uso
print("\nRecorrido DFS (Iterativo):")
dfs_iterativo(grafo, 'A')  # Comenzamos desde el nodo 'A'