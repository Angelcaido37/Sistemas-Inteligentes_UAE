# Algoritmo DFS - Versión recursiva

# Definimos el grafo como un diccionario de listas
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def dfs_recursivo(grafo, nodo, visitados=None):
    if visitados is None:
        visitados = set()
    
    if nodo not in visitados:
        print(nodo, end=" ")
        visitados.add(nodo)

        for vecino in grafo[nodo]:
            dfs_recursivo(grafo, vecino, visitados)

# Ejemplo de uso:
print("\nRecorrido DFS (Recursivo):")
dfs_recursivo(grafo, 'A')

