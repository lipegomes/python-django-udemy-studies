# # 48. Exercícios propostos

# """
# 1 - Crie uma função que exibe uma saudação com os parâmetros saudação e nome.
# """


# def saudacao(saudacao='', nome=''):
#     print(f'{saudacao} {nome}')


# saudacao('Olá', 'Filipe')


# """
# 2 - Crie uma função que recebe 3 números como parâmetros
# e exiba a soma entre eles.
# """


# def soma(n1, n2, n3):
#     print(n1 + n2 + n3)


# soma(1, 2, 3)


# """
# 3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo
# um percentual (ex.10%). Retorne (return) o valor do primeiro número somado
# do aumento do percentual do mesmo.
# """


# def aumento_perc(valor, percentual):
#     return valor + (valor * percentual / 100)


# ap = aumento_perc(100, 25)
# print(ap)


"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz, se
o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne
o número enviado.
"""


def fb_1(n1=""):
    n1 = int(input("Digite um número inteiro: "))

    if n1 % 3 == 0 and n1 % 5 == 0:
        print(f"fizzbuzz, {n1} é divisível por 3 e 5")
    elif n1 % 3 == 0:
        print(f"fizz, {n1} é divisível por 3")
    elif n1 % 5 == 0:
        print(f"buzz, {n1} é divisível por 5")
    else:
        print(n1)


fb_1()


def fb_2(n2):
    if n2 % 3 == 0 and n2 % 5 == 0:
        return f"fizzbuzz, {n2} é divisível por 3 e 5"
    elif n2 % 3 == 0:
        return f"fizz, {n2} é divisível por 3"
    elif n2 % 5 == 0:
        return f"buzz, {n2} é divisível por 5"
    else:
        return n2


print(fb_2(15))
