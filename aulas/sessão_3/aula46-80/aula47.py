# 47. Funções (def) em Python - Parte 2


def value(var):
    print("This will not be performed")
    return var


variable = value("Value I want")

if variable:
    print(variable)
else:
    print("No value.")


def division(n1="", n2="", result=""):
    n1 = float(input("Enter a number: "))
    n2 = float(input("Enter other number: "))
    result = n1 / n2

    if n2 > 0:
        print(result)
    elif n2 < 0:
        print(result)
    else:
        print("Conta inválida")


division()


def dumb():
    return [1, 2, 3, 4, 5]


qst = dumb()
print(dumb(), type(qst))
