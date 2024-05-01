nome = "carlos henrique"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "  Olá Mundo!  "

print("|" + texto.strip() + "|")
print("|" + texto.rstrip() + "|")
print("|" + texto.lstrip() + "|")

menu = "Python"

print("|" + menu.center(12, "#") + "|")

print(".".join(menu.center(12, "#")))
print(".".join(texto))
print(".".join(nome))
