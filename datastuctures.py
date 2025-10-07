# Estructuras de Datos en Python

# Arreglos (Listas)
# Creación de un "arreglo" (lista)
mi_array = [10, 20, 30, 40, 50]

# Acceso rápido a un elemento por su índice (O(1))
print(f"Elemento en el índice 2: {mi_array[2]}") # Salida: 30

# Inserción de un elemento (requiere desplazar elementos, O(n))
mi_array.insert(1, 15)
print(f"Array después de insertar: {mi_array}") # Salida: [10, 15, 20, 30, 40, 50]

# Eliminación de un elemento (requiere desplazar elementos, O(n))
mi_array.pop(3)
print(f"Array después de eliminar: {mi_array}") # Salida: [10, 15, 20, 40, 50]


# Listas enlazadas

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
    
    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

# Uso
mi_lista_enlazada = ListaEnlazada()
mi_lista_enlazada.agregar(10)
mi_lista_enlazada.agregar(20)
mi_lista_enlazada.agregar(30)
mi_lista_enlazada.imprimir() # Salida: 10 -> 20 -> 30 -> None




#stacks 
mi_pila = []

# Push (agregar)
mi_pila.append(1)
mi_pila.append(2)
mi_pila.append(3)
print(f"Pila: {mi_pila}") # Salida: [1, 2, 3]

# Pop (quitar)
elemento_quitado = mi_pila.pop()
print(f"Elemento quitado: {elemento_quitado}") # Salida: 3
print(f"Pila ahora: {mi_pila}") # Salida: [1, 2]

# Tablas Hash (Diccionarios)
# Creación de un diccionario (tabla hash)
mi_tabla_hash = {"nombre": "Juan", "edad": 30, "ciudad": "Bogotá"}

# Acceso, inserción y modificación (promedio O(1))
print(f"Edad: {mi_tabla_hash['edad']}") # Salida: 30
mi_tabla_hash["profesion"] = "Ingeniero" # Agregar
mi_tabla_hash["edad"] = 31 # Modificar

print(f"Tabla Hash completa: {mi_tabla_hash}")

# Eliminación
del mi_tabla_hash["ciudad"]
print(f"Tabla después de eliminar: {mi_tabla_hash}")



##Colas con deque
from collections import deque

mi_cola = deque()

# Enqueue (agregar)
mi_cola.append(1)
mi_cola.append(2)
mi_cola.append(3)
print(f"Cola: {mi_cola}") # Salida: deque([1, 2, 3])

# Dequeue (quitar del principio)
elemento_quitado = mi_cola.popleft()
print(f"Elemento quitado: {elemento_quitado}") # Salida: 1
print(f"Cola ahora: {mi_cola}") # Salida: deque([2, 3])


#trees
class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None 
def insertar_nodo(raiz, dato):
    if raiz is None:
        return NodoArbol(dato)
    else:
        if dato < raiz.dato:
            raiz.izquierda = insertar_nodo(raiz.izquierda, dato)
        else:
            raiz.derecha = insertar_nodo(raiz.derecha, dato)
    return raiz 
def inorder(raiz):
    if raiz:
        inorder(raiz.izquierda)
        print(raiz.dato, end=" ")
        inorder(raiz.derecha)   
# Uso
raiz = None     
raiz = insertar_nodo(raiz, 50)
insertar_nodo(raiz, 30)
insertar_nodo(raiz, 70)
insertar_nodo(raiz, 20)     
insertar_nodo(raiz, 40)
insertar_nodo(raiz, 60)

insertar_nodo(raiz, 80)
print("Recorrido Inorder del árbol:")
inorder(raiz) # Salida: 20 30 40 50 60 70 80
print()   


#graphs
class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_arista(self, u, v):
        if u not in self.grafo:
            self.grafo[u] = []
        if v not in self.grafo:
            self.grafo[v] = []
        self.grafo[u].append(v)
        self.grafo[v].append(u) # Para grafo no dirigido

    def imprimir_grafo(self):
        for nodo in self.grafo:
            print(f"{nodo} -> {', '.join(map(str, self.grafo[nodo]))}")
# Uso
mi_grafo = Grafo()      
mi_grafo.agregar_arista(1, 2)
mi_grafo.agregar_arista(1, 3)
mi_grafo.agregar_arista(2, 4)
mi_grafo.agregar_arista(3, 4)
mi_grafo.imprimir_grafo()
# Salida: 
# 1 -> 2, 3
# 2 -> 1, 4
# 3 -> 1, 4
# 4 -> 2, 3

#graphs with adjacency list
mi_grafo_lista = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4],
    4: [2, 3]
}
print(f"Grafo con lista de adyacencia: {mi_grafo_lista}")
# Salida: Grafo con lista de adyacencia: {1: [2, 3], 2: [1, 4], 3: [1, 4], 4: [2, 3]}

def agregar_arista_lista(grafo, u, v):
    grafo.setdefault(u, []).append(v)
    grafo.setdefault(v, []).append(u) # Para grafo no dirigido  
agregar_arista_lista(mi_grafo_lista, 4, 5)
print(f"Grafo actualizado: {mi_grafo_lista}")   
# Salida: Grafo actualizado: {1: [2, 3], 2: [1, 4], 3: [1, 4], 4: [2, 3, 5], 5: [4]}