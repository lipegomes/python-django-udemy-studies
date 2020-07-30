# 30. While - estrutura de repetição em Python

# while True:
#     nome = input("Qual o seu nome? ")
#     print(f"Olá {nome}!")
#     break

# x = 0
# while x < 10:
#     if x == 3:
#         x += 1
#         break

#     print(x)
#     x += 1

# print("Acabou")

while True:
    print()
    num1 = input("Digite um número: ")
    num2 = input("Digite outro número: ")
    operador = input("Digite um operador: ")
    sair = input("Deseja sair? [s]im ou [n]ão: ")

    if sair == "s":
        break

    if not num1.isnumeric() or not num2.isnumeric():
        print("Você precisa digitar um número.")
        continue

    num1 = int(num1)  # type cast
    num2 = int(num2)  # type cast

    # + -  / *
    if operador == "+":
        print(num1 + num2)
    elif operador == "-":
        print(num1 - num2)
    elif operador == "/":
        print(num1 / num2)
    elif operador == "*":
        print(num1 * num2)
    else:
        print(f"O operador {operador} digitado é invalido.")
