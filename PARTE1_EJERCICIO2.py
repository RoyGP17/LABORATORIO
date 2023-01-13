print("==========Programa de Notas==========")

def calificaciones():
    notas = [20, 15, 12, 11, 8, 4, 1]
    Nota_baja = notas[0]
    Indice_bajo = 0

    for i in range(1, len(notas)):
        if notas[i] < Nota_baja:
            Nota_baja = notas[i]
            Indice_bajo = i

    notas.pop(Indice_bajo)
    print("La notas son: ",notas)

    promedio = sum(notas) / len(notas)
    print("El promedio es: ", promedio)

calificaciones()