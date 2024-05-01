def sacar():
    if saldo >= saque:
        mensagem = "valor sacado!"
    else:
        mensagem = "saldo indisponível"
    return mensagem

saldo = 2000.0
saque = float(input("Informe o valor do saque: "))
print(sacar())
