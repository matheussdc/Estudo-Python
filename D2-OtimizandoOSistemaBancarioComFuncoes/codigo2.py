import textwrap


def saque():  # Keyword only (*,)
    return None


def deposito():  # Positional only (,/)
    return None


def extrato(saldo, /, *, extrato):
    return None


def criar_usuario(): # Nome, data de nascimento, CPF, endereço = "logradouro - nro - bairro - cidade/sigla"
    return None


def criar_conta_corrente(): # Agência, nro da conta, usuário
    return None


def main():
    menu = """
    MENU
    [1] - Depósito
    [2] - Saque
    [3] - Extrato
    [q] - Sair
    Selecione uma operação: """

    saldo = 0                    # Saldo inicial = 0
    extrato_historico = []       # Extrato com registro de depósitos e saques por String
    saque_limite_valor = 500.00  # Limite de saque diário R$500.00
    saque_limite_vezes = 3       # No máximo 3 saques por dia

    while True:
        operation = input(textwrap.dedent(menu))

        if operation == '1':
            deposito()

        elif operation == '2':
            saque()

        elif operation == '3':
            extrato()

        elif operation == 'q':
            print("Saída")
            break

        else:
            print("Operação Inválida!!")


if __name__ == '__main__':
    main()
