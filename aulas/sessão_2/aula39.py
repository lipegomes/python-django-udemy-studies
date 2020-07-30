# 39. Operação ternária em Python

logged_user = True
msg = "Usuário logado." if (logged_user) else "Usuário precisa fazer loguin."

print(msg)

print("----****----")

idade = input("Qual a sua idade? ")

if not idade.isnumeric():
    print("Você precisa digitar apenas números")
else:
    idade = int(idade)
    maior_idade = idade >= 18
    msg = "Pode acessar" if maior_idade else "Não pode acessar"

    print(msg)
