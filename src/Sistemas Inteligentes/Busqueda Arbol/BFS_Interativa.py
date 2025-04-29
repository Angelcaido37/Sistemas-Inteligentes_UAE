from collections import deque

# Función para BFS
def bfs(grafo, inicio):
    """
    Realiza un recorrido BFS e imprime los nodos visitados.
    :param grafo: Diccionario que representa el grafo (lista de adyacencia).
    :param inicio: Nodo inicial desde donde comenzar el recorrido.
    """
    visitados = set()  # Conjunto para llevar registro de nodos visitados
    cola = deque([inicio])  # Cola para simular el recorrido BFS ( Los nodos se agregan al final de la cola y se extraen desde el principio (FIFO))

    while cola:
        nodo = cola.popleft()  # Extraemos el primer nodo de la cola
        if nodo not in visitados: #Este conjunto asegura que no visitemos el mismo nodo más de una vez, evitando ciclos infinitos.
            visitados.add(nodo)
            print(nodo, end=" ")  # Imprimimos el nodo visitado

            # Exploramos los vecinos del nodo actual
            for vecino in grafo[nodo]: #Para cada nodo visitado, exploramos sus vecinos. Si un vecino no ha sido visitado, lo añadimos a la cola.
                if vecino not in visitados:
                    cola.append(vecino)

# Grafo de ejemplo (lista de adyacencia)
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Ejecutar el recorrido BFS
print("Recorrido BFS:")
bfs(grafo, 'A')  # Comenzamos desde el nodo 'A'