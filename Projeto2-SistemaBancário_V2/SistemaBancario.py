menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valorDeposito = float(input("Qual o valor do depósito?  "))
        if (valorDeposito > 0):
            saldo += valorDeposito
            extrato += f"Depósito: R$ {valorDeposito:.2f}\n"
            print (f"Foram depositados R$ {valorDeposito}.")
        else:
            print("Valor de depósito inválido, favor selecionar novamente a operação desejada.")

    elif opcao == "2":
        valorSaque = float(input("Qual o valor do saque?  "))
        if (valorSaque > 0):
            if (LIMITE_SAQUES > 0):
                if (valorSaque < saldo):
                    if (valorSaque < limite):
                        saldo -= valorSaque
                        extrato += f"Saque: R$ {valorSaque:.2f}\n"
                        LIMITE_SAQUES -= 1
                        print (f"Foram sacados R$ {valorSaque}. {LIMITE_SAQUES} saques diários restantes.")
                    else:
                        print("Saque acima do limite permitido, favor selecionar novamente a operação desejada.")
                else:
                    print("Saldo insuficente, favor selecionar novamente a operação desejada.")
            else:
                print("Limite diário de saques atingido, favor selecionar a operação desejada.")
        else:
            print("Valor de saque inválido, favor selecionar novamente a operação desejada.")

    elif opcao == "3":
        print("\n========================EXTRATO========================")
        print("Não foram encontradas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n=======================================================")
        

    elif opcao == "0":
        break

    else:
        print("Operação invláida, favor selecionar novamente a operação desejada.")