print("========== Programa de matrices ==========")

print("Suma de matrices")
def suma_matriz(matriz1, matriz2):
    # Crear una nueva matriz para almacenar el resultado de la suma
    resultado = []

    for i in range(len(matriz1)):
        nueva_matriz = []
        for j in range(len(matriz2[0])):
            nueva_matriz.append(0)
        resultado.append(nueva_matriz)

    # Recorrer cada elemento de ambas matrices y sumarlos
    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            resultado[i][j] = matriz1[i][j] + matriz2[i][j]

    return resultado

matriz1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matriz2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

resultado = suma_matriz(matriz1, matriz2)

for i in resultado:
    print(i)

#%%
print("Resta de matrices")

def resta_matriz(matriz1, matriz2):
    # Crear una nueva matriz para almacenar el resultado de la resta
    resultado = []

    for i in range(len(matriz1)):
        nueva_matriz = []
        for j in range(len(matriz2[0])):
            nueva_matriz.append(0)
        resultado.append(nueva_matriz)

    # Recorrer cada elemento de ambas matrices y restarlos
    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            resultado[i][j] = matriz1[i][j] - matriz2[i][j]

    return resultado

matriz1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matriz2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]
resultado = resta_matriz(matriz1, matriz2)

for i in resultado:
    print(i)
