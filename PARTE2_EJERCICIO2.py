print("===========Programa de matrices==========")
print("Multiplicaciones de matrices")
def multiplicacion_matriz(matriz1, matriz2):
    # Crear una nueva matriz para almacenar el resultado de la multiplicación
    resultado = []

    for i in range(len(matriz1)):
        nueva_matriz = []
        for j in range(len(matriz2[0])):
            nueva_matriz.append(0)
        resultado.append(nueva_matriz)

    # Recorrer cada elemento de ambas matrices y multiplicarlos
    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz2)):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]

    return resultado

matriz1 = [[1, 2, 3],
           [4, 5, 6]]
matriz2 = [[7, 8],
           [9, 10],
           [11, 12]]

resultado = multiplicacion_matriz(matriz1, matriz2)

for i in resultado:
    print(i)