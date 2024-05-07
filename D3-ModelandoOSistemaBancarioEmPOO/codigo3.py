import textwrap
from abc import ABC, abstractproperty, abstractclassmethod


class Conta:
    def __init__(self, cliente, numero):
        self._saldo = 0
        self._numero = numero
        self._agencia = "Bradesco"
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)

    def sacar(self, valor):
        if valor > self._saldo:
            print("Não há saldo suficiente para o saque desejado")
            return False
        if valor > 0:
            self._saldo -= valor
            self._historico.adicionar_transacao(Saque(valor))
            return True

    def depositar(self, valor):
        return 4


class ContaCorrente(Conta):
    def __init__(self, agencia, cliente, limite=500.00, limite_saques=3):
        super().__init__(agencia, cliente)
        self.limite = limite
        self.limite_saques = limite_saques


class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta, transacao):
        return None

    def adicionar_conta(self, conta):
        self._contas.append(conta)


class PesosaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_de_nascimento):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_de_nascimento = data_de_nascimento


class Historico:
    def __init__(self):
        self._transacoes = []

    def adicionar_transacao(self, transacao):
        self._transacoes.append(transacao)
        return True


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        return self._valor


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        return self._valor


def main():
    print("Hello World")


if __name__ == '__main__':
    main()
