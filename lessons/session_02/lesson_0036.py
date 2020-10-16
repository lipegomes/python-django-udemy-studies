# 36. Split, Join e Enumerate em Python
"""
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # iteráveis
"""
print("------------------------------------------------------------------")

string = "O futuro pertence aqueles que acreditam na beleza dos seus sonhos."
lista1 = string.split(" ")
lista2 = string.split(",")

print(lista1)
print(lista2)

for valor in lista1:
    print(valor)

print("------------------------------------------------------------------")

for valor in lista2:
    print(valor)

print("------------------------------------------------------------------")

for valor in lista1:
    print(f"A palavra '{valor}' apareceu {lista1.count(valor)}x na frase")

print("------------------------------------------------------------------")

palavra = ""
contagem = 0
for valor in lista1:
    qtd_vezes = lista1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f"A palavra que apareceu mais vezes é {palavra} ({contagem})x")

print("------------------------------------------------------------------")

frase = "Setembro é o melhor mês do ano!!!"
lista3 = frase.split(" ")

for indice, valor in enumerate(lista3):
    print(indice, valor)

print("------------------------------------------------------------------")

lista4 = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 10],
]

for v in lista4:
    print(v[0], v[1])

print("------------------------------------------------------------------")
