# 113. Desafio POO

"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco
tem clientes e contas.

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
"""
from banco import Banco
from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca


banco = Banco()

client1 = Cliente("Gregorio", 57)
client2 = Cliente("Joana", 35)
client3 = Cliente("Maria", 18)

conta1 = ContaPoupanca(1111, 457812, 5000)
conta2 = ContaCorrente(3333, 453567, 0)
conta3 = ContaPoupanca(4789, 457812, 0)

client1.inserir_conta(conta1)
client2.inserir_conta(conta2)
client3.inserir_conta(conta3)

banco.inserir_cliente(client1)
banco.inserir_conta(conta1)

banco.inserir_cliente(client2)
banco.inserir_conta(conta2)

banco.inserir_cliente(client3)
# banco.inserir_conta(conta3)

if banco.autenticar(client1):
    client1.conta.sacar(150)
else:
    print("Cliente não autenticado.")

print()

if banco.autenticar(client2):
    client2.conta.sacar(200)
else:
    print("Cliente não autenticado.")

print()

if banco.autenticar(client3):
    client3.conta.depositar(1000)
else:
    print("Cliente não autenticado.")
