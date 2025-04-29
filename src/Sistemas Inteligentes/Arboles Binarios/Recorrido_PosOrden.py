# Definición de un árbol binario
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def recorrido_post_orden_iterativo(raiz):
    """
    Realiza un recorrido posterior al orden iterativo de un árbol binario.
    :param raiz: Nodo raíz del árbol.
    """
    if raiz is None:
        return
    
    pila = []
    nodo_actual = raiz
    visitados = set()

    while pila or nodo_actual:
        while nodo_actual:
            pila.append(nodo_actual)
            nodo_actual = nodo_actual.izquierda

        nodo_actual = pila[-1]  # Nodo en la cima de la pila

        # Si el nodo no tiene hijo derecho o ya fue visitado
        if nodo_actual.derecha is None or nodo_actual.derecha in visitados:
            print(nodo_actual.valor, end=" ")  # Visitar el nodo
            visitados.add(nodo_actual)
            pila.pop()
            nodo_actual = None  # Reiniciar nodo_actual
        else:
            nodo_actual = nodo_actual.derecha  # Moverse al subárbol derecho

# Ejemplo de uso
if __name__ == "__main__":
    # Construir un árbol binario
    """
    Árbol construido:
            4
           / \
          2   6
         / \ / \
        1  3 5  7
    """
    raiz = Nodo(4)
    raiz.izquierda = Nodo(2)
    raiz.derecha = Nodo(6)
    raiz.izquierda.izquierda = Nodo(1)
    raiz.izquierda.derecha = Nodo(3)
    raiz.derecha.izquierda = Nodo(5)
    raiz.derecha.derecha = Nodo(7)


# Ejemplo de uso
print("\nRecorrido posterior al orden (iterativo):")
recorrido_post_orden_iterativo(raiz)