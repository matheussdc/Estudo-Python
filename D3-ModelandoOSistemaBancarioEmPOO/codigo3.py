# import textwrap
from abc import ABC, abstractmethod


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

    @property
    def historico(self):
        return self.historico

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
        print("Valor inválido para saque!!")
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self._historico.adicionar_transacao(Deposito(valor))
            return True
        print("Valor inválido para depósito!!")
        return False


class ContaCorrente(Conta):
    _saques_realizados = 0

    def __init__(self, agencia, cliente, limite=500.00, limite_saques=3):
        super().__init__(agencia, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        if self._saques_realizados >= self._limite_saques:
            print("Limite de saque diário atingido!!")
            return False
        if valor > self._limite:
            print(f"Valor limite de R$ {self._limite:.2f} de saque ultrapassado!!")
            return False
        super().sacar(valor)
        self._saques_realizados += 1
        return True


class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta, transacao):
        if conta in self._contas:
            transacao.registrar(conta)
            return True
        print("Conta não pertence a este cliente!!")
        return False

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
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        deposito_validado = conta.depositar(self._valor)
        if deposito_validado:
            conta.historico.adicionar_transacao(self)
            return True
        return False


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        saque_validado = conta.sacar(self._valor)
        if saque_validado:
            conta.historico.adicionar_transacao(self)
            return True
        return False


def main():
    print("Hello World")


if __name__ == '__main__':
    main()
