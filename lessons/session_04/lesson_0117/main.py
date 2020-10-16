# 117. Dataclasses

"""
O que são dataclasses? O módulo Dataclasses fornece um decorador e funções
para criar automaticamente métodos, como __init__(), __repr__(), __eq__ (etc)
em classes definidas pelo usuário.
Basicamente, dataclasses são syntax sugar para criar classes normais.
Foi originalmente descrito na PEP 557.
Adicionado na versão 3.7 do Python.
Leia a documentação: https://docs.python.org/pt-br/3/library/dataclasses.html
"""
from dataclasses import dataclass
from dataclasses import field
from dataclasses import asdict, astuple


@dataclass(eq=True, repr=True, order=True, frozen=False, init=True)
class Pessoa:
    nome: str
    sobrenome: str
    # sobrenome: str = field(repr=False)

    def __post_init__(self):
        # self.nome_completo = f'{self.nome} {self.sobrenome}'
        if not isinstance(self.nome, str):
            raise TypeError(
                f"Tipo inválido {type(self.nome).__name__} != str em {self}."
            )

    @property  # getter
    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"


print("-" * 120)

cliente1 = Pessoa("Urek", "Mazino")
cliente2 = Pessoa("Androssi", "Zahard")

print(cliente1)
print(cliente1.nome)
print(cliente1.sobrenome)
print(cliente1.nome_completo)

print("-" * 120)

print(cliente1 == cliente2)

print("-" * 120)

p1 = Pessoa("A", "Mazino")
p2 = Pessoa("B", "Luffy")
p3 = Pessoa("C", "Senna")
p4 = Pessoa("D", "Capone")

pessoas1 = [p1, p2, p3, p4]

print(sorted(pessoas1))

print("-" * 120)

n1 = Pessoa("A", "7")
n2 = Pessoa("B", "3")
n3 = Pessoa("C", "2")
n4 = Pessoa("D", "9")

numeros = [n1, n2, n3, n4]

print(sorted(numeros, key=lambda pessoa: pessoa.sobrenome, reverse=True))

print("-" * 120)

p5 = Pessoa("F", "Mazino")
p6 = Pessoa("G", "Luffy")
p7 = Pessoa("H", "Senna")
p8 = Pessoa("I", "Capone")
# p8 = Pessoa(5698, 'Capone')

pessoas2 = [p5, p6, p7, p8]

print(sorted(pessoas2, key=lambda pessoa: pessoa.sobrenome, reverse=True))

print("-" * 120)

print(asdict(p1))
print(astuple(p7))

print("-" * 120)
