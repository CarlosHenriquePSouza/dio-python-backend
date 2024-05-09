menu = '''
 ### Menu ###
 [n] Novo Cliente
 [c] Criar Conta
 [l] Listar Contas
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
clientes = []
contas = []
AGENCIA = "0001"

def novo_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("Cliente já cadastrado com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Cliente cadastrado com sucesso!")

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def criar_conta(agencia, numero_conta, clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente}

    print("Cliente não encontrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['cliente']['nome']}
        """
        print("=" * 100)
        print(linha)

def depositar(saldo, deposito, extrato, /):
    if deposito <= 0:
        print("Depósito inválido.\nValor de depósito deve ser maior que zero!")
    else:
        saldo += deposito
        extrato += f''' Depósito: R$ {deposito:10.2f}\n'''
        print("Depósito executado com sucesso!")
    return saldo, extrato

def sacar(*, saldo, saque, extrato, limite, numero_saques, limite_saques):
    if saldo <= 0:
        print("Saque não permitido.\nSaldo da conta menor ou igual a zero!")
    elif numero_saques >= limite_saques:
        print("Saque não permitido.\nO número de saques permitido foi atingido!")
    elif saque > limite:
        print(f"Saque não permitido.\nO valor máximo de saque permitido é de R$ {limite:.2f}")
    elif saque > saldo:
        print("Saque não permitido.\nSaque maior que o saldo da conta")
    else:
        saldo -= saque
        numero_saques += 1
        extrato += f'''    Saque: R$ {saque:10.2f}\n'''
        print("Saque executado com sucesso!")
    return saldo, extrato, numero_saques

def extratp(saldo, /, *, extrato):
    print("\n" + " Extrato Bancário ".center(24, "#"))
    print()
    print("Sem movimentações\n" if not extrato else extrato)
    print("########################")
    print(f"    Saldo: R$ {saldo:10.2f}")
    print("########################")


while True:

    opcao = input(menu)

    if opcao == "n":
        novo_cliente(clientes)

    elif opcao == "c":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, clientes)

        if conta:
            contas.append(conta)

    elif opcao == "l":
        listar_contas(contas)

    elif opcao == "d":
        deposito = float(input("Valor de depósito: "))
        saldo, extrato = depositar(saldo, deposito, extrato)

    elif opcao == "s":
        saque = float(input("Valor do Saque: "))
        saldo, extrato, numero_saques = sacar(saldo=saldo, 
                                              saque=saque, 
                                              extrato=extrato, 
                                              limite=limite, 
                                              numero_saques=numero_saques, 
                                              limite_saques=LIMITE_SAQUES)

    elif opcao == "e":
        extrato(saldo, extrato=extrato)

    elif opcao == "q":
        print("Fim da aplicação!")
        break

    else:
        print("Opção inválida")
