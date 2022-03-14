# Python avançado função enumerate 

lista = ["abacate", "bola", "cachorro"]
"""
for i in range(len(lista)): # range cria um vetor, len mede o tamanho
    print(i, lista[i])
"""

# Esta é a forma correta de fazer em python:

for i, nome in enumerate(lista):
    print(i, nome)