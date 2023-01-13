print("==========Programa de matrices==========")
def almacenando():
    entrada = int(input("Endique el tamaño de la lista: "))
    lista1 = []
    lista2 = []

    for i in range(entrada):

        nombres = input("Diga los nombres de las personas: ")
        lista1.append(nombres)
        lista2.append(len(nombres))

    print(lista1)
    print(lista2)

almacenando()