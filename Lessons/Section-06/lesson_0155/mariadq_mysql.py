import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='571401',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        yield conexao
    finally:
        # print('Conexão fechada')
        conexao.close()


# # executa a conexão
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES ' \
#               '(%s, %s, %s, %s)'
#         cursor.execute(sql, ('Kanguru', 'Jack', 25, 148))
#         conexao.commit()


# # executa a conexão
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES ' \
#               '(%s, %s, %s, %s)'

#         dados = [
#             ('Airton', 'Senna', 34, 72),
#             ('Monkey', 'D. Luffy', 19, 70),
#             ('Gol', 'D. Roger', 53, 180)
#         ]

#         cursor.executemany(sql, dados)
#         conexao.commit()

# # deleta um id
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id = %s'
#         cursor.execute(sql, (6,))
#         conexao.commit()

# # deleta três id.
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
#         cursor.execute(sql, (1, 2, 3))
#         conexao.commit()

# # deleta id entre um intervalo %s AND s%
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
#         cursor.execute(sql, (4, 6))
#         conexao.commit()

# atualiza um id inserindo novos dados
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
        cursor.execute(sql, ('UREK', 9))
        conexao.commit()

# executa o SELECT
with conecta() as conexao:
    with conexao.cursor() as cursor:
        # seleciona tudo no banco de dados
        # cursor.execute('SELECT * FROM clientes')
        # seleciona nome e sobrenome
        # cursor.execute('SELECT nome, sobrenome FROM clientes')
        # seleciona nome e sobrenome os renomeando(não é boa prática em prog.)
        # cursor.execute('SELECT nome as n, sobrenome as sn FROM clientes')
        # seleciona em ordem decrescente e limita a 100 dicionários
        # cursor.execute('SELECT * FROM clientes ORDER BY id DESC LIMIT 100')
        # seleciona em ordem crescente e limita a 100 dicionários
        cursor.execute('SELECT * FROM clientes ORDER BY id ASC LIMIT 100')
        resultado = cursor.fetchall()

        for linha in resultado:
            # imprime todos os resultados
            print(linha)
            # imprime nome, sobrenome, peso
            # print(linha['nome'], linha['sobrenome'], linha['peso'])
            # imprime nome, sobrenome
            # print(linha['nome'], linha['sobrenome'])
            # imprime nome[n], sobrenome[sn]
            # print(linha['n'], linha['sn'])

# cursor.close()
# conexao.close()
