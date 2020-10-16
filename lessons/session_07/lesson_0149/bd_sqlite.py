import sqlite3

conexao = sqlite3.connect("basededados.db")
cursor = conexao.cursor()

# # criando tabela clientes com dados: id, nome, peso.
# cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'nome TEXT,'
#                'peso REAL'
#                ')')

# # Insenrindo registro dentro da tabela clientes.
# # Está forma facilita Sql Injection
# cursor.execute(
#     'INSERT INTO clientes (nome, peso) VALUES ("Ronaldinho Gaucho", 74.8)'
# )
# # Está forma ajuda a previnir Sql Injection
# cursor.execute(
#     'INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria', 54)
# )
# # Utilizando dicionários
# cursor.execute(
#     'INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
#     {'nome': 'Petter', 'peso': 100}
# )
# # Utilizando VALUES
# cursor.execute(
#     'INSERT INTO clientes VALUES(:id, :nome, :peso)',
#     {'id': None, 'nome': 'Wendy', 'peso': 50}
# )
# conexao.commit()

# # mudar o nome em um determinado id
# cursor.execute(
#     'UPDATE clientes SET nome=:nome WHERE id=:id',
#     {'nome': 'Barbara', 'id': 1}
# )
# conexao.commit()

# # excluir o nome em um determinado id
# cursor.execute(
#     'DELETE FROM clientes WHERE id=:id',
#     {'id': 1}
# )
# conexao.commit()

# # seleção
# cursor.execute('SELECT * FROM clientes')

# for linha in cursor.fetchall():
#     # print(linha)
#     identificador, nome, peso = linha

#     print(identificador, nome, peso)

# # selecionando peso > 50
# cursor.execute('SELECT nome, peso FROM clientes WHERE peso > 50')

# for linha in cursor.fetchall():
#     # print(linha)
#     nome, peso = linha

#     print(nome, peso)

# selecionando peso > 80
cursor.execute("SELECT nome, peso FROM clientes WHERE peso > :peso", {"peso": 80})

for linha in cursor.fetchall():
    # print(linha)
    nome, peso = linha

    print(nome, peso)

cursor.close()
conexao.close()
