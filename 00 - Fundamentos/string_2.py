nome = "Carlos Henrique"
idade = 28
profissao = "Analista de Sistemas"
linguagem = "Delphi"
saldo = 450.514

dados = {"nome": "Carlos Henrique", "idade": 28}

print("Nome: %s Idade: %d" % (nome, idade))

print("Nome: {} Idade: {}".format(nome, idade))

print("Nome: {1} Idade: {0}".format(idade, nome))

print("Nome: {campo1} Idade: {campo2}".format(campo2=idade, campo1=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")
