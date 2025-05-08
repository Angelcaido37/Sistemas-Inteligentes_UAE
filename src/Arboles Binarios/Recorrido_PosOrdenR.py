# Definición de un árbol binario
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Función para el recorrido posterior al orden
def recorrido_post_orden(nodo):
    """
    Si el nodo no es None, primero se recorre recursivamente el subárbol izquierdo.
    Luego, se recorre recursivamente el subárbol derecho.
    Finalmente, se visita el nodo actual imprimiendo su valor.
    """
    if nodo is not None:
        # 1. Recorrer el subárbol izquierdo
        recorrido_post_orden(nodo.izquierda)
        
        # 2. Recorrer el subárbol derecho
        recorrido_post_orden(nodo.derecha)
        
        # 3. Visitar el nodo actual
        print(nodo.valor, end=" ")

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

    # Realizar el recorrido posterior al orden
    print("Recorrido posterior al orden:")
    recorrido_post_orden(raiz)