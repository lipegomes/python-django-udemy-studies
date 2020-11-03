# 32. Iterando strings com while em Python

minha_string = (
    "Acordar cedo torna o dia mais produtivo " + "e cuidar do corpo ébom para a saúde."
)

tamanho_string = len(minha_string)

print(minha_string.count("a"))

# Contador
c = 0

nova_string = ""

while c < tamanho_string:
    # Tornando a letra 'a' maiúscula com upper()
    if minha_string[c] == "a":
        nova_string += minha_string[c].upper()
    else:
        nova_string += minha_string[c]

    c += 1

print(nova_string)


while True:
    minha_string = input("Digite uma frase: ")
    tamanho_string = len(minha_string)

    c = 0

    contagem_atual = 0
    letra = ""
    while c < tamanho_string:
        qdt_vezes_letra = minha_string.count(minha_string[c])

        if contagem_atual < qdt_vezes_letra and minha_string[c].strip():
            letra = minha_string[c]
            contagem_atual = qdt_vezes_letra

        c += 1

    print(f"A letra '{letra}' foi digitada {contagem_atual} vezes.")
    break
