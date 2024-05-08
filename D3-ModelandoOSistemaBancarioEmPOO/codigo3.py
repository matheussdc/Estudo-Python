import textwrap
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
        return self._historico

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)

    def sacar(self, valor):
        if valor > self._saldo:
            print("Não há saldo suficiente para o saque desejado")
            return False
        if valor > 0:
            self._saldo -= valor
            return True
        print("Valor inválido para saque!!")
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
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
        saque_validado = super().sacar(valor)
        if saque_validado:
            self._saques_realizados += 1
            return True
        return False


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


class PessoaFisica(Cliente):
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
    # Instanciação simples de PessoaFisica
    pessoa1 = PessoaFisica("Av dos Bobos, 123", "123123123", "Pedro Monte", "12/08/2013")
    # Instanciação e associação de uma ContaCorrente a uma PessoaFisica
    cc1 = ContaCorrente("Bradesco", pessoa1, 400.00, 3)
    pessoa1.adicionar_conta(cc1)

    # Realiza um depósito de 500,00 na ContaCorrente cc1
    pessoa1.realizar_transacao(cc1, Deposito(4321.56))
    print(f"#Saldo atual da conta cc1 = {cc1.saldo} após depósito inicial")

    # Realiza um depósito inválido com valor negativo
    pessoa1.realizar_transacao(cc1, Deposito(-3.14))
    print(f"#Saldo atual da conta cc1 = {cc1.saldo} após depósito inválido")

    # Realiza um saque válido
    pessoa1.realizar_transacao(cc1, Saque(21.56))
    print(f"#Saldo atual da conta cc1 = {cc1.saldo} após primeiro saque válido")

    # Realiza um saque inválido acima do limite de saque
    pessoa1.realizar_transacao(cc1, Saque(401.00))
    print(f"#Saldo atual da conta cc1 = {cc1.saldo} após saque acima do limite")

    # Realiza um saque inválido com valor negativo
    pessoa1.realizar_transacao(cc1, Saque(-3.14))
    print(f"#Saldo atual da conta cc1 = {cc1.saldo} após saque inválido")

    # Realiza segundo saque válido
    pessoa1.realizar_transacao(cc1, Saque(102.00))
    print(f"#Saldo atual da conta cc1 = {cc1.saldo} após segundo saque válido")

    # Realiza terceiro e último possível saque válido
    pessoa1.realizar_transacao(cc1, Saque(103.00))
    print(f"#Saldo atual da conta cc1 = {cc1.saldo} após terceiro saque válido")

    # Realiza um saque inválido acima do limite diário de saques
    pessoa1.realizar_transacao(cc1, Saque(104.00))
    print(f"#Saldo atual da conta cc1 = {cc1.saldo} após tentativa de saque acima do limite diário")


if __name__ == '__main__':
    main()
