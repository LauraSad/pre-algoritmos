# 1. Variables y tipos de datos.
nombre_plataforma = 'Leetcode'  #String
problemas_resueltos = 0         #Numero (Integer)
estudiando = True               #Booleano
tiempo_estimado = 1.5           #Numero (Float)

print(f"Variable tipo String:{nombre_plataforma}")
print(f"Variable tipo número:{problemas_resueltos}")
print(f"Variable tipo booleano:{estudiando}")

#2. Estructuras condicionales: if, elif, else

if problemas_resueltos == 0:
    print("A empezar con el primer problema")
elif problemas_resueltos < 10:
    print("Buen comienzo, a seguir practicando")
else:
    print("Ya eres un pro")

#3. Bucles: for y while
plataformas = ["HackerRank", "LeetCode", "CodeSignal"]
print("\nPlataformas de practica:")
for plataforma in plataformas:
    print(f"-{plataforma}")

contador_pomodoro = 0
print("\nIniciando sesión de estudio (bucle while):")
while contador_pomodoro < 3:
    contador_pomodoro += 1
    print(f"Completado Pomodoro #{contador_pomodoro}")

# 4. Funciones
def verificar_eficiencia(nombre_algoritmo, complejidad):
    """
    Una funcion simple que recibe el nombre de un algoritmo
    y su complejidad para retornar un mensaje
    """   
    return f"El algoritmo '{nombre_algoritmo}' tienen una complejidad de {complejidad}."

# Llamada a la función
mensaje = verificar_eficiencia("Busqueda Binaria", "O(log n)")
print(f"\nProbando la funcion = {mensaje}") 
