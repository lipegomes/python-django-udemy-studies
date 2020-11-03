# 99. Associação - Python Orientado a Objetos

from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor("Pearson")
print(escritor.nome)

caneta = Caneta("Compactor")
print(caneta.marca)

maquina = MaquinaDeEscrever()
maquina.escrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()
