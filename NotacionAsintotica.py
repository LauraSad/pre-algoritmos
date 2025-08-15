
lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5] #o(1)

def encontrar_maximo(lista): ## O(1)
    if not lista:    
        return None  # Retorna None si la lista está vacía O(1)
    maximo = lista[0] # O(1)
    for numero in lista: ## O(n)
        if numero > maximo: #O(n)
            maximo = numero #O(n)
    return maximo   # O(1) Solo se ejecuta una vez al final
print("El máximo de la lista es:", encontrar_maximo(lista))    #O(1)