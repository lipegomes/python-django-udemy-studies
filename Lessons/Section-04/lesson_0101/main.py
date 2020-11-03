# 101. Composição - Python Orientado a Objetos

from classes import Cliente, Endereco


cliente1 = Cliente("João", 50)
cliente1.insere_endereco("São Paulo", "SP")
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()

cliente2 = Cliente("Maria", 42)
cliente2.insere_endereco("Curitiba", "PR")
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente2
print()

cliente3 = Cliente("José", 19)
cliente3.insere_endereco("Belo Horizonte", "MG")
print(cliente3.nome)
cliente3.lista_enderecos()
del cliente3
print()

print("*" * 20)
