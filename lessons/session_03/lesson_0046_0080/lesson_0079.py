# 79. Uso de try e except como condicional


def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass


while True:
    num = converte_numero(input("Digite um número: "))

    if num is None:
        print(f"Error: '{num}' não é número")
    else:
        print(num * 5)
