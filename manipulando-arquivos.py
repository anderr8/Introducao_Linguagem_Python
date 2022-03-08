# -*- coding: UTF-8 -*-
# arquivo = open("meu-arquivo.txt")

# linhas = arquivo.readlines()

# print(linhas)

"""
for linha in linhas:
    print(linha)
"""
"""
texto_completo = arquivo.read()
print(texto_completo)
"""
"""
w = open("meu-arquivo2.txt", "w")

w.write("Esse é o meu arquivo\n")

w.close() # sempre fechar o arquivo
"""

arquivo = open("meu-arquivo.txt")

texto_completo = arquivo.read()
print(texto_completo)

"""
w = open("meu-arquivo.txt", "w")

w.write("Meu arquivo:\n")
w.write("Olá, Mundo!")

w.close()
"""

