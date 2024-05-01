MAIOR_IDADE = 18
IDADE_COM_SUPERVISAO = 16

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade >= IDADE_COM_SUPERVISAO:
    print("Pode tirar a CNH mas tem que dirigir com um responsável.")
else:
    print("Ainda não pode tirar a CNH.")