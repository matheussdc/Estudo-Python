import textwrap


def main():
    menu = """\
    MENU
    [1] - Depósito
    [2] - Saque
    [3] - Extrato
    [q] - Sair
    Selecione uma operação: """

    saldo = 0                   #Saldo inicial = 0
    extrato_historico = []                #Extrato com registro de depósitos e saques por String
    saque_limite_valor = 500.00 #Limite de saque diário R$500.00
    saque_limite_vezes = 3      #No máximo 3 saques por dia

    while True:
        operation = input(textwrap.dedent(menu))

        if operation == '1':
            print("Depósito - ", end="")
            while True:
                try:
                    valor_depositado = float(input("Insira a quantidade a ser depositada: R$"))
                    if valor_depositado > 0:
                        saldo += valor_depositado
                        extrato_historico.append(f"Depósito de R$ {valor_depositado:.2f}")
                        break
                    else:
                        print("Valor inválido para depósito!! - ", end="")
                except ValueError:
                    print("Valor inválido para depósito!! - ", end="")

        elif operation == '2':
            if saque_limite_vezes == 0:
                print("Limite de saque diário atingido !!")
                continue

            print("Saque - ", end="")
            while True:
                try:
                    valor_sacado = float(input("Insira a quantidade a ser sacada: R$"))
                    if valor_sacado > saque_limite_valor:
                        print(f"Valor limite de {saque_limite_valor:.2f} de saque ultrapassado!! - ", end="")
                    elif valor_sacado > saldo:
                        print("Não há saldo suficiente para o saque desejado")
                        break
                    elif valor_sacado > 0:
                        saldo -= valor_sacado
                        extrato_historico.append(f"Saque de R$ {valor_sacado:.2f}")
                        saque_limite_vezes -= 1
                        break
                    else:
                        print("Valor inválido para saque!! - ", end="")
                except ValueError:
                    print("Valor inválido para saque!! - ", end="")

        elif operation == '3':
            print("Extrato")

        elif operation == 'q':
            print("Saída")
            break

        else:
            print("Operação Inválida!!")


if __name__ == '__main__':
    main()
