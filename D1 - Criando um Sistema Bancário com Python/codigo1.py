import textwrap


def main():
    menu = """\
    MENU
    [1] - Depósito
    [2] - Saque
    [3] - Extrato
    [q] - Sair
    Selecione uma operação: """

    saldo = 0     #Saldo inicial = 0
    extrato = []  #Extrato com registro de depósitos e saques por String

    while True:
        operation = input(textwrap.dedent(menu))

        if operation == '1':
            print("Depósito - ", end="")
            while True:
                try:
                    valor_depositado = float(input("Insira a quantidade a ser depositada: R$"))
                    if valor_depositado > 0:
                        saldo += valor_depositado
                        extrato.append(f"Depositados R$ {valor_depositado:.2f}")
                        break
                    else:
                        print("Valor inválido para depósito!! - ", end="")
                except ValueError:
                    print("Valor inválido para depósito!! - ", end="")

        elif operation == '2':
            print("Saque")

        elif operation == '3':
            print("Extrato")

        elif operation == 'q':
            print("Saída")
            break

        else:
            print("Operação Inválida!!")


if __name__ == '__main__':
    main()
