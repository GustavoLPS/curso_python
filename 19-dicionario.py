meu_dicionario = {"A": "AMEIXA", "B": "BOLA", "C": "CACHORRO"}

print(meu_dicionario["A"])

for chave in meu_dicionario:
    print(chave + "-" + meu_dicionario[chave])

for i in meu_dicionario.items():
    print(i)

for i in meu_dicionario.keys():
    print(i)

for i in meu_dicionario.values():
    print(i)