texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra.upper(), end="")
    else:
        print(letra, end="")
else:
    print()

# Exemplo utilizando a função built-in range
for numero in range(0, 51, 5):
    print(numero, end=" ")
print()
for numero in range(0, 71, 7):
    print(numero, end=" ")    
print()