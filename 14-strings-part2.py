a = "Gustavo"
b = "Pinheiro"

concatenar = a + " " + b
print(concatenar)
print(concatenar.lower())
print(concatenar.upper())
concatenar = concatenar.upper()
print(concatenar)

concatenar = a + " " + b + "\n"
print(concatenar.strip())

minha_string = "O rato roeu a roupa do rei de Roma"

minha_lista = minha_string.split(" ")
minha_lista2 = minha_string.split("r")
print(minha_lista)
print(minha_lista2)

busca = minha_string.find("rei")
print(busca)
print(minha_string[busca:])

minha_string = minha_string.replace("o rei", "a rainha")
print(minha_string)