"""
Considerando duas listas de inteiros o floats (lista A ou lista B)
Some os valores nas listas retomando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar
o tamanho da menor.

Exemplo:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

==== resultado ====
lista_soma = [2, 4, 6, 8]
"""
from itertools import zip_longest

#  zip só une as listas até o tamanho da menor lista
lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma1 = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma1)  # Saída: [22, 4, 6, 10, 55]

# zip_longest captura os valores da lista maior.
lista_c = [10, 2, 3, 4, 5]
lista_d = [12, 2, 3, 6, 50, 60, 70]
lista_soma2 = [x + y for x, y in zip_longest(lista_c, lista_d, fillvalue=0)]
print(lista_soma2)  # Saída: [22, 4, 6, 10, 55, 60, 70]

# Neste caso, usamos o "fillvalue" como 0 (zero), assim conseguimos capturar
# os valores restantes da lista maior, realizando contas, sem obter um erro
# em nosso programa.
lista_e = [1, 2, 3, 4, 5]
lista_f = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8]
lista_soma3 = [x + y for x, y in zip_longest(lista_e, lista_f, fillvalue=0)]
print(lista_soma3)
