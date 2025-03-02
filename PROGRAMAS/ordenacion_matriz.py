# Definimos la matriz 3x3
matriz = [
    [9, 2, 5],
    [4, 7, 1],
    [8, 3, 6]
]

# Función para ordenar una fila específica de la matriz usando Bubble Sort
def ordenar_fila(matriz, fila):
    n = len(matriz[fila])
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if matriz[fila][j] > matriz[fila][j + 1]:
                # Intercambiamos los elementos
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]

# Mostramos la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Fila que queremos ordenar (0-based index)
fila_a_ordenar = 1

# Llamamos a la función para ordenar la fila
ordenar_fila(matriz, fila_a_ordenar)

# Mostramos la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)