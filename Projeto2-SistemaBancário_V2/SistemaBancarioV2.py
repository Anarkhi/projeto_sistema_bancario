import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tCriar Novo Usuário
    [5]\tCriar Nova Conta
    [6]\tListar Contas
    [0]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valorDeposito, extrato, /):
    if valorDeposito > 0:
        saldo += valorDeposito
        extrato += f"Depósito: R$ {valorDeposito:.2f}\n"
        print (f"\nForam depositados R$ {valorDeposito}.")
    else:
        print("Valor de depósito inválido, favor selecionar novamente a operação desejada.")

    return saldo, extrato

def sacar(*,saldo, valorSaque, extrato, limite, limite_saques):
    if (valorSaque > 0):
        if (limite_saques > 0):
            if (valorSaque < saldo):
                if (valorSaque < limite):
                    saldo -= valorSaque
                    extrato += f"Saque: R$ {valorSaque:.2f}\n"
                    LIMITE_SAQUES -= 1
                    print (f"\nue acima do limite permitido, favor selecionar novamente a operação desejada.")
            else:
                print("\nSaldo insuficente, favor selecionar novamente a operação desejada.")
        else:
            print("\nLimite diário de saques atingido, favor selecionar a operação desejada.")
    else:
        print("\nValor de saque inválido, favor selecionar novamente a operação desejada.")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n========================EXTRATO========================")
    print("Não foram encontradas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n=======================================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return

    nome = input("\nInforme o nome completo: ")
    data_nascimento = input("\n a data de nascimento (dd-mm-aaaa): ")
    endereco = input("\nInforme o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"\nnome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")
    
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['\nnome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():

    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "1":
            valorDeposito = float(input("Qual o valor do depósito?  "))

            saldo, extrato = depositar(saldo, valorDeposito, extrato)
        
        elif opcao == "2":
            valorSaque = float(input("Qual o valor do saque?  "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valorSaque,
                extrato=extrato,
                limite=limite,
                #numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
            
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("Operação invláida, favor selecionar novamente a operação desejada.")

main()