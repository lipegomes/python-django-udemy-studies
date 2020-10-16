import sqlite3


class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, telefone):
        # insere valores
        consulta = "INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)"
        # executa consulta para inserir valores
        self.cursor.execute(consulta, (nome, telefone))
        # commit salva os valores
        self.conn.commit()

    def editar(self, nome, telefone, id):
        # edita valores
        consulta = "UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?"
        # executa consulta
        self.cursor.execute(consulta, (nome, telefone, id))
        # commit salva os valores
        self.conn.commit()

    def excluir(self, id):
        # deleta valores
        consulta = "DELETE from agenda WHERE id=?"
        # executa consulta para deletar valores
        self.cursor.execute(consulta, (id,))
        # commit salva os valores
        self.conn.commit()

    def listar(self):
        self.cursor.execute("SELECT * FROM agenda")

        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        consulta = "SELECT * FROM agenda WHERE nome LIKE ?"
        self.cursor.execute(consulta, (f"%{valor}%",))

        for linha in self.cursor.fetchall():
            print(linha)

    # fechar a conexão
    def fechar(self):
        self.cursor.close()
        self.conn.close()


if __name__ == "__main__":
    agenda = AgendaDB("agenda.db")
    # inserir nomes e telefones no banco de dados
    # agenda.inserir('Mike', '00120-3000')
    # agenda.inserir('Jonny', '01030-2000')
    # agenda.inserir('Maria', '02940-1000')
    # agenda.inserir('Claudia', '03850-0000')
    # agenda.inserir('Fernanda', '04760-9000')
    # agenda.inserir('Pedro', '05670-8000')
    agenda.inserir("João Silva", "01789-5647")
    agenda.inserir("Silva Junior", "03447-2582")
    agenda.inserir("Helena Silva", "06789-3444")
    agenda.inserir("Maria Silva", "02845-6784")
    # editar nomes, telefone, id
    # agenda.editar('Helena', '08321-2747', 14)
    # excluir contato
    # agenda.excluir(17)
    # agenda.listar()
    agenda.buscar("silva")
