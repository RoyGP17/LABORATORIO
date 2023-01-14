print("===========Programa de matrices===========")

def matriz_diagonal():
    matriz = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    n = len(matriz)
    for i in range(n):
        print(matriz[i][i])

    diagonal = []
    n = len(matriz)
    for i in range(n):
        diagonal.append(matriz[i][i])

matriz_diagonal()