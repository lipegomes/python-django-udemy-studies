# 100. Agregação - Python Orientado a Objetos

from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto("Camisa Azul", 20)
p2 = Produto("Calça Jeans", 50)
p3 = Produto("Sapato", 120)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)

carrinho.lista_produto()
print(f"\nTotal: R$ {carrinho.soma_total()}")
