# 34. Listas em Python

"""
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
print("----****----")

lista = ["A", "B", "C", "D", "E"]
print(lista)

lista.append("F")
print(lista)

lista.insert(6, "G")
print(lista)

lista.pop(2)
print(lista)

del lista[0:3]
print(lista)

lista.clear()
print(lista)

print("----****----")


l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(min(l1))
print(max(l1))

l2 = list(range(0, 100, 8))

for valor in l2:
    print(valor)

print("----****----")

l3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

soma = 0
for valor in l3:
    soma += valor

print(soma)


print("----****----")

l4 = ["String", True, 10, -22.4]

for el in l4:
    print(f"O tipo de el é {type(el)} e o seu valor é {el} ")


print("----****----")

secreta = "perfume"
digitadas = []
chances = 3

while True:
    if chances < 0:
        print("Você perdeu !!!")
        break

    letra = input("Digite uma letra: ")

    if len(letra) > 1:
        print("Ah isso não vale, digite apenas uma letra.")
        continue

    digitadas.append(letra)

    if letra in secreta:
        print(f"A letra '{letra}' digitada existe na palavra secreta.")
    else:
        print(f"A letra '{letra}' digitada não existe na palavra secreta.")
        digitadas.pop()

    secreta_temp = ""
    for letra_secreta in secreta:
        if letra_secreta in digitadas:
            secreta_temp += letra_secreta
        else:
            secreta_temp += "*"

    if secreta_temp == secreta:
        print(f"Que legal, VOCÊ GANHOU!!! A palavra secreta era: {secreta_temp}.")
    else:
        print(f"A palavra secreta está assim: {secreta_temp}")

    if letra not in secreta:
        chances -= 1

    print(f"Você ainda tem {chances} chances.")
    print()
