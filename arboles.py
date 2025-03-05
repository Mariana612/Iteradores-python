

class Nodo:
    def __init__(self,data, izq = None, der = None):
        self.data = data
        self.izq = izq
        self.der = der

arbol = Nodo(5,Nodo(4),Nodo(7,Nodo(6)))

def iterador(nodo):
    if nodo is not None:                            #Se chequea que el nodo no sea none. Condicion de salida
        yield from iterador(nodo.izq)               #Recorrido de la rama izquierda 

        yield nodo.data                             #Se hace yield del dato almacenado en el nodo
        
        yield from iterador(nodo.der)               #recorrido de rama derecha


for i in iterador(arbol):
    print(i)