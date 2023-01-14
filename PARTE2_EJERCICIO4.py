print("==========Programa matrices==========")

def matriz_transpuesta():
    matriz = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    transpuesta = []
    for i in range(len(matriz[0])):
        fila = []
        for j in range(len(matriz)):
            fila.append(matriz[j][i])
        transpuesta.append(fila)

    for fila in transpuesta:
        for elemento in fila:
            print(elemento, end=' ')
        print()
matriz_transpuesta()