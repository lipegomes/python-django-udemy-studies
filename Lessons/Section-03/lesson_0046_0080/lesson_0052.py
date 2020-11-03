# 52. Exercícios propostos

"""
1 - Crie uma funcao1 que receba uma funcao2 como parâmetro e
retorne o valor da funcao2 executada
"""


def funcao1():
    return "Olá mundo!"


def funcao2(funcao1):
    return funcao1()


executando = funcao2(funcao1)
print(executando)


"""
2 - Crie uma funcao1 que recebe uma funcao2 como parâmetro e retorne o valor
da funcao2 executada. Faça a funcao1 executar duas funções que recebam um
número diferente de argumentos.
"""


def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f"Oi {nome}"


def saudacao(nome, saudacao):
    return f"{saudacao} {nome}"


executando1 = mestre(fala_oi, "Luffy")
executando2 = mestre(saudacao, "Luffy", saudacao="Bom dia!")
print(executando)
print(executando2)
