# 57. Sistema de perguntas e respostas com dicionários em Python

print("Orientações:")
print("* Cada pergunta tem quatro alternativas [a],[b],[c],[d] de respostas.")
print("** Somente UMA das alternativas é a CORRETA.")
print(f"Total de acerto >= 60% -> APROVADO")
print(f"Total de acerto < 60% -> REPROVADO")


perguntas = {
    "Pergunta 1": {
        "pergunta": "Quanto é 2+2?",
        "respostas": {"a": "1", "b": "4", "c": "7", "d": "0"},
        "resposta_certa": "b",
    },
    "Pergunta 2": {
        "pergunta": "Quanto é 10-2?",
        "respostas": {"a": "8", "b": "9", "c": "5", "d": "12"},
        "resposta_certa": "a",
    },
    "Pergunta 3": {
        "pergunta": "Quanto vale a raiz de 100?",
        "respostas": {"a": "5", "b": "9", "c": "11", "d": "10"},
        "resposta_certa": "d",
    },
    "Pergunta 4": {
        "pergunta": "Qual o valor de 9**2?",
        "respostas": {"a": "18", "b": "72", "c": "81", "d": "90"},
        "resposta_certa": "c",
    },
    "Pergunta 5": {
        "pergunta": "Quantos quadrantes existem no plano cartesiano?",
        "respostas": {"a": "4", "b": "1", "c": "nenhum", "d": "2"},
        "resposta_certa": "a",
    },
}
print()

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f"{pk}: {pv['pergunta']}")

    print("Escolha uma das opções abaixo:")
    for rk, rv in pv["respostas"].items():
        print(f"[{rk}]: {rv}")

    resposta_usuario = input("Sua resposta: ")

    if resposta_usuario == pv["resposta_certa"]:
        print("Resposta correta!")
        respostas_certas += 1
    else:
        print("Resposta errada!")

    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f"Você acertou {respostas_certas} respostas.")
print(f"Sua porcentagem de acerto foi de {porcentagem_acerto}%.")

total_acerto = porcentagem_acerto

if total_acerto >= 60:
    print(f"Parabéns, você foi APROVADO(A) com {total_acerto} pontos.")
else:
    print(
        f"Você foi REPROVADO(A) com {total_acerto} pontos. "
        f"Te vejo no próximo semestre"
    )
