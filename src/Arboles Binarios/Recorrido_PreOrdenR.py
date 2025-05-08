# Definición de un árbol binario
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Función para el recorrido en pre-orden
def recorrido_pre_orden(nodo):
    """
    Función recorrido_pre_orden:
    Si el nodo no es None, primero se visita el nodo actual imprimiendo su valor.
    Luego, se recorre recursivamente el subárbol izquierdo.
    Finalmente, se recorre recursivamente el subárbol derecho.
    """
    if nodo is not None:
        # 1. Visitar el nodo actual
        print(nodo.valor, end=" ")
        
        # 2. Recorrer el subárbol izquierdo
        recorrido_pre_orden(nodo.izquierda)
        
        # 3. Recorrer el subárbol derecho
        recorrido_pre_orden(nodo.derecha)

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

    # Realizar el recorrido en pre-orden
    print("Recorrido en pre-orden:")
    recorrido_pre_orden(raiz)