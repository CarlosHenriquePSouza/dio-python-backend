menu = '''
 ### Menu ###
 [d] Depositar
 [s] Sacar
 [e] Extrato
 [q] Sair

 => '''

saldo = 0
limite =  500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Valor de depósito: "))
        if deposito <= 0:
            print("Depósito inválido.\nValor de depósito deve ser maior que zero!")
            continue
        saldo += deposito
        extrato += f''' Depósito: R$ {deposito:10.2f}\n'''
        print("Depósito executado com sucesso!")

    elif opcao == "s":
        if saldo <= 0:
            print("Saque não permitido.\nSaldo da conta menor ou igual a zero!")
            continue
        if numero_saques >= LIMITE_SAQUES:
            print("Saque não permitido.\nO número de saques permitido foi atingido!")
            continue
        saque = float(input("Valor de Saque: "))
        if saque > limite:
            print(f"Saque não permitido.\nO valor máximo de saque permitido é de R$ {limite:.2f}")
            continue
        if saque > saldo:
            print("Saque não permitido.\nSaque maior que o saldo da conta")
            continue
        saldo -= saque
        numero_saques += 1
        extrato += f'''    Saque: R$ {saque:10.2f}\n'''
        print("Saque executado com sucesso!")

    elif opcao == "e":
        print("\n" + " Extrato Bancário ".center(24, "#"))
        print()
        print("Sem movimentações\n" if not extrato else extrato)
        print("########################")
        print(f"    Saldo: R$ {saldo:10.2f}")
        print("########################")

    elif opcao == "q":
        print("Fim da aplicação!")
        break

    else:
        print("Opção inválida")

