# 59. Exercício

"""
-> É uma lista de listas de números inteiros
-> As listas internas tem o tamanho de 10 elementos
-> As listas internas contém números entre 1 a 10 e eles
podem ser duplicados.

-> Crie uma função que encontra o primeiro número duplicado
na lista interna.
    Requisitos:
        A ordem dos números duplicados é considerada a partir
        da segunda ocorrencia (o número duplicado em si).
        Exemplo: [1, 2, 3 ->3<-, 2, 1] 3
        Se não encontrar duplicados na lista, retorne -1
"""
lista = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]


def encontra_duplicado(duplicado):
    numeros_checados = set()
    primeiro_duplicado = "Não tem duplicado"

    for numero in duplicado:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break

        numeros_checados.add(numero)

    return primeiro_duplicado


for lista_de_inteiros in lista:
    print(lista_de_inteiros, encontra_duplicado(lista_de_inteiros))
