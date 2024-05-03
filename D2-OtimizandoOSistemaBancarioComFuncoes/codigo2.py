import textwrap


def saque(*, saldo, limite_vezes, limite_valor, extrato_hist):  # Keyword only (*,)
    if limite_vezes == 0:
        print("Limite de saque diário atingido !!")
        return None

    print("Saque - ", end="")
    while True:
        try:
            valor_sacado = float(input("Insira a quantidade a ser sacada: R$"))
            if valor_sacado > limite_valor:
                print(f"Valor limite de {limite_valor:.2f} de saque ultrapassado!! - ", end="")
            elif valor_sacado > saldo:
                print("Não há saldo suficiente para o saque desejado")
                break
            elif valor_sacado > 0:
                saldo -= valor_sacado
                extrato_hist.append(f"Saque de R$ {valor_sacado:.2f}")
                limite_vezes -= 1
                return saldo, limite_vezes
            elif valor_sacado == 0:
                return None
            else:
                print("Valor inválido para saque!! - ", end="")
        except ValueError:
            print("Valor inválido para saque!! - ", end="")


def deposito(saldo, valor, extrato_hist, /):  # Positional only (,/)
    saldo += valor
    extrato_hist.append(f"Depósito de R$ {valor:.2f}")
    return saldo


def extrato(saldo, /, *, extrato_hist):
    if extrato_hist:
        for movimentacao in extrato_hist:
            print(movimentacao)
    else:
        print("Não foram realizadas movimentações")
    print(f"Saldo disponível: R$ {saldo:.2f}")


# Nome, data de nascimento, CPF, endereço = "logradouro - nro - bairro - cidade/estado"
def criar_usuario(lista_usuarios):
    cpf_novo = input("Criar Usuário - Insira o CPF do novo usuário: ")  # Sem tratar a validade
    for cpf, user in lista_usuarios:
        if cpf_novo == cpf:
            print("Usuário já cadastrado!!")
            return None
    nome = input("Insira o nome do novo usuário: ")
    data = input("Insira a data de nascimento do novo usuário: ")
    logradouro = input("Insira o logradouro do novo usuário: ")
    numero = input("Insiro número do endereço do novo usuário: ")
    bairro = input("Insira o bairro do novo usuário: ")
    cidade = input("Insira a cidade do novo usuário: ")
    estado = input("Insira o estado do novo usuário: ")
    endereco = {"logradouro": logradouro, "numero": numero, "cidade": cidade, "bairro": bairro, "estado": estado}
    novo_usuario = (cpf_novo, {"nome": nome, "nascimento": data, "endereço": endereco})
    return novo_usuario


def listar_usuarios(lista_usuarios):
    print("Usuários:")
    if lista_usuarios:
        for cpf, user in lista_usuarios:
            nome, data, endereco = user.values()
            log, num, city, bairro, estado = endereco.values()
            print(f"{cpf}: Nome: {nome}, Nascimento: {data}, Endereço: {log} - {num} - {bairro} - {city}/{estado}")
    else:
        print("Não há usuários cadastrados")


def criar_conta_corrente(lista_usuarios, numero_conta): # Agência, nro da conta, usuário
    cpf_user = input("Criar Conta Corrente - Insira o CPF do usuário: ")
    for cpf, user in lista_usuarios:
        if cpf_user == cpf:
            numero_conta += 1
            conta = (numero_conta, {"agência": "0001", "CPF": cpf_user})
            return conta, numero_conta
    print("Usuário não existe!!")
    return None, numero_conta


def listar_contas(lista_contas):
    print("Contas Correntes:")
    if lista_contas:
        for numero, conta in lista_contas:
            agencia, cpf = conta.values()
            print(f"Conta Nº {numero} - Agencia {agencia} - CPF: {cpf}")
    else:
        print("Não há contas registradas")


def main():
    menu = """
    MENU
    [1] - Depósito
    [2] - Saque
    [3] - Extrato
    [4] - Criar Usuário
    [5] - Listar Usuários
    [6] - Criar Conta Corrente
    [7] - Listar Contas
    [q] - Sair
    Selecione uma operação: """
    lista_usuarios = []          # Lista com os usuários cadastrados
    lista_contas = []            # Lista com as contas correntes registradas
    total_contas = 0
    saldo = 0                    # Saldo inicial = 0
    extrato_historico = []       # Extrato com registro de depósitos e saques por String
    saque_limite_valor = 500.00  # Limite de saque diário R$500.00
    saque_limite_vezes = 3       # No máximo 3 saques por dia

    while True:
        operation = input(textwrap.dedent(menu))

        if operation == '1':
            print("Depósito - ", end="")
            while True:
                try:
                    valor_depositado = float(input("Insira a quantidade a ser depositada: R$"))
                    if valor_depositado > 0:
                        saldo = deposito(saldo, valor_depositado, extrato_historico)
                        break
                    elif valor_depositado == 0:
                        break
                    else:
                        print("Valor inválido para depósito!! - ", end="")
                except ValueError:
                    print("Valor inválido para depósito!! - ", end="")

        elif operation == '2':
            saldo, saque_limite_vezes = saque(saldo=saldo, limite_vezes=saque_limite_vezes, limite_valor=saque_limite_valor, extrato_hist=extrato_historico)

        elif operation == '3':
            extrato(saldo, extrato_hist=extrato_historico)

        elif operation == '4':
            novo_usuario = criar_usuario(lista_usuarios)
            if novo_usuario is not None:
                lista_usuarios.append(novo_usuario)

        elif operation == '5':
            listar_usuarios(lista_usuarios)

        elif operation == '6':
            nova_conta, total_contas = criar_conta_corrente(lista_usuarios, total_contas)
            if nova_conta is not None:
                lista_contas.append(nova_conta)

        elif operation == '7':
            listar_contas(lista_contas)

        elif operation == 'q':
            print("Saída")
            break

        else:
            print("Operação Inválida!!")


if __name__ == '__main__':
    main()
