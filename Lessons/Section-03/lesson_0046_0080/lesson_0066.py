# 66. Exercício proposto

carrinho = []

carrinho.append(("Produto 1", 30.50))
carrinho.append(("Produto 2", 20))
carrinho.append(("Produto 3", 50))

# List Comprehension
total = sum([float(v) for p, v in carrinho])

print(f"R$ {total}")
