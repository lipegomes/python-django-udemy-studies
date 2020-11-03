from contextlib import contextmanager


@contextmanager
def abrir(arquivo, modo):
    try:
        print("Abrindo arquivo")
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        print("Fechando arquivo")
        arquivo.close()


with abrir("novo.txt", "w") as arquivo:
    arquivo.write("Linha 1\n")
    arquivo.write("Linha 2\n")
    arquivo.write("Linha 3\n")
    arquivo.write("Linha 4\n")
    arquivo.write("Linha 5\n")
    arquivo.write("Linha 6\n")
    arquivo.write("Linha 7\n")
    arquivo.write("Linha 8\n")
    arquivo.write("Linha 9\n")
    arquivo.write("Linha 10\n")
