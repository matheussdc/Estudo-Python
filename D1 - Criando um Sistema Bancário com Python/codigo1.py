import textwrap


def main():
    menu = """\
    MENU
    [1] - Depósito
    [2] - Saque
    [3] - Extrato
    [q] - Sair
    Selecione uma operação: """

    while True:
        operation = input(textwrap.dedent(menu))

        if operation == '1':
            print("Depósito")

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
