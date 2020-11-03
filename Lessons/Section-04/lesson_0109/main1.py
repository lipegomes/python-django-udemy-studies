# 109. Context Manager - Criando e Usando gerenciadores de contexto


# with open("frase.txt", "w") as file:
#     file.write("O dia está lindo !!!")

# self.data_base = {
#     'name': 'Filipe',
#     'age': 28,
#     'birthday': '09/18/1991',
#     'city': 'Duque de Caxias',
#     'state': 'Rio de Janeiro',
#     'country': 'Brasil',
#     'occupation': 'Student'
# }


class Arquivo:
    def __init__(self, arquivo, modo):
        print("abrindo arquivo")
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print("retornando arquivo")
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("fechando arquivo")
        self.arquivo.close()
        # print(exc_type)
        # print(exc_val)
        # print(exc_tb)


with Arquivo("abc.txt", "w") as arquivo:
    arquivo.write("O dia está fresco e o céu está azul.")
