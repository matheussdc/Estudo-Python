import textwrap


def saque():  # Keyword only (*,)
    return None


def deposito():  # Positional only (,/)
    return None


def extrato(saldo, /, *, extrato):
    return None


# Nome, data de nascimento, CPF, endereço = "logradouro - nro - bairro - cidade/estado"
def criar_usuario(lista_usuarios):
    cpf = input("Criar Usuário - Insira o CPF do novo usuário: ")  # Sem tratar a validade
    if cpf in lista_usuarios:
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
    novo_usuario = {cpf: {"nome": nome, "nascimento": data, "endereço": endereco}}
    return novo_usuario


def listar_usuarios(lista_usuarios):
    print("Usuários:")
    if lista_usuarios:
        for cpf, user in lista_usuarios.items():
            nome, data, endereco = user.values()
            log, num, city, bairro, estado = endereco.values()
            print(f"{cpf}: Nome: {nome}, Nascimento: {data}, Endereço: {log} - {num} - {bairro} - {city}/{estado}")
    else:
        print("Não há usuários cadastrados")


def criar_conta_corrente(): # Agência, nro da conta, usuário
    return None


def main():
    menu = """
    MENU
    [1] - Depósito
    [2] - Saque
    [3] - Extrato
    [4] - Criar Usuário
    [5] - Listar Usuários
    [q] - Sair
    Selecione uma operação: """
    lista_usuarios = {}
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
            extrato(2, extrato=3)

        elif operation == '4':
            novo_usuario = criar_usuario(lista_usuarios)
            if novo_usuario is not None:
                lista_usuarios.update(novo_usuario)

        elif operation == '5':
            listar_usuarios(lista_usuarios)

        elif operation == 'q':
            print("Saída")
            break

        else:
            print("Operação Inválida!!")


if __name__ == '__main__':
    main()
