# 50. Funções (def) em Python - Parte 3 - *args **kwargs


def func_1(*args):  # Tupla
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))


func_1(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def func_2(*args, **kwargs):  # Tupla
    print(args)
    print(kwargs["nome"], kwargs["sobrenome"])


lista1 = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func_2(*lista1, *lista2, nome="D.Luffy", sobrenome="Monkey")


def func_3(*args, **kwargs):  # Tupla
    print(args)

    nome = kwargs.get("nome")
    print(nome)

    sobrenome = kwargs.get("sobrenome")
    print(sobrenome)

    idade = kwargs.get("idade")

    if idade is not None:
        print(idade)
    else:
        print("Idade não existe")


lista3 = [1, 2, 3, 4, 5]
lista4 = [10, 20, 30, 40, 50]
func_3(*lista3, *lista4, nome="D.Luffy", sobrenome="Monkey")
