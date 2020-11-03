class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome  # _private
        self._idade = idade  # _private

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None

    def inserir_conta(self, conta):
        self.conta = conta
