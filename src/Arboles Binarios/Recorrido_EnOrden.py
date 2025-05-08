# Definición de un árbol binario
class Nodo: #Representa un nodo en el árbol binario. Cada nodo tiene un valor y dos hijos: uno a la izquierda y otro a la derecha.
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Función para el recorrido en orden
def recorrido_en_orden(nodo):
    """
    Función recorrido_en_orden:
    Si el nodo no es None, primero se recorre el subárbol izquierdo recursivamente.
    Luego, se visita el nodo actual imprimiendo su valor.
    Finalmente, se recorre el subárbol derecho recursivamente.
    """
    if nodo is not None:
        # 1. Recorrer el subárbol izquierdo
        recorrido_en_orden(nodo.izquierda)
        
        # 2. Visitar el nodo actual
        print(nodo.valor, end=" ")
        
        # 3. Recorrer el subárbol derecho
        recorrido_en_orden(nodo.derecha)

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

    # Realizar el recorrido en orden
    print("Recorrido en orden:")
    recorrido_en_orden(raiz)