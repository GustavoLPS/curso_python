# -*- coding: utf-8 -*-

# lendo arquivo
arquivo = open("arquivo.txt")

linhas = arquivo.readlines()

for linha in linhas:
    print(linha)

texto_completo = arquivo.read()
print(texto_completo)

# criando e escrevendo no arquivo
w = open("arquivo2.txt", "w")
w.write("Esse é o meu arquivo")
w.close()

w = open("arquivo.txt", "a")
w.write("Esse é o meu arquivo\n")
w.close()