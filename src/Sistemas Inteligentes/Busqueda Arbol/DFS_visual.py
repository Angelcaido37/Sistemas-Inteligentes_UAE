import networkx as nx
import matplotlib.pyplot as plt

# Función recursiva para DFS
def dfs_recursivo(grafo, nodo, visitados, arbol_dfs):
    visitados.add(nodo)

    for vecino in grafo[nodo]:
        if vecino not in visitados:
            # Añadimos la arista al árbol DFS
            arbol_dfs.add_edge(nodo, vecino)
            dfs_recursivo(grafo, vecino, visitados, arbol_dfs)

# Grafo de ejemplo (lista de adyacencia)
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Crear un grafo dirigido con NetworkX
G = nx.DiGraph()

# Añadir aristas al grafo
for nodo, vecinos in grafo.items():
    for vecino in vecinos:
        G.add_edge(nodo, vecino)

# Inicializar variables para el DFS
visitados = set()
arbol_dfs = nx.DiGraph()  # Árbol DFS resultante

# Realizar el recorrido DFS
dfs_recursivo(grafo, 'A', visitados, arbol_dfs)

# Dibujar el grafo original
plt.figure(figsize=(12, 6))

# Subplot 1: Grafo original
plt.subplot(1, 2, 1)
plt.title("Grafo Original")
pos = nx.spring_layout(G)  # Posiciones para el grafo
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=800)

# Subplot 2: Árbol DFS
plt.subplot(1, 2, 2)
plt.title("Árbol DFS")
nx.draw(arbol_dfs, pos, with_labels=True, node_color='lightgreen', edge_color='blue', node_size=800)

# Mostrar la visualización
plt.tight_layout()
plt.show()