menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depòsito: R$ {valor:.2f}\n"
        else:
            print("valor informado é invalido.")

    elif opcao == "2":
        valor = float(input("Informe o valor que deseja sacar: "))

        execedeu_saldo = valor > saldo

        execedeu_limite = valor > limite

        execedeu_saque = valor >= LIMITE_SAQUE

        if execedeu_saldo:
            print("Saldo insuficiente")
        elif execedeu_limite:
            print("o valo desejado execede o limite de saque")

        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saque += 1

        else:
            print("operação falhou! o valor informado é invalido")

    elif opcao == "3":
        print("\n ############ EXTRATO ############")
        print("\n Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\n saldo: R$ {saldo:.2f}")
        print("####################################")

    elif opcao == "4":
        break

    else:
        print("Opção não reconhecida pelo sistema, por favor selecione novamente a operação desejada")