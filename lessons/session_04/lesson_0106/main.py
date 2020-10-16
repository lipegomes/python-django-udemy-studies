# 106. Criando Exceções - Python Orientado a Objetos


# Por convenção toda excessão termina com Error.
class HighError(Exception):
    pass


def test():
    raise HighError("Too many algorithms per line !!!")


try:
    test()
except HighError as error:
    print(f"Error: {error}")
