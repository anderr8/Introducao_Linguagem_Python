
meu_dicionario = {"A": "AMEIXA", "B": "BOLA", "C": "CACHORRO"} # → dicionários sem são declarados entre {}

"""
print(meu_dicionario["A"]) # → colchetes são usados para encontrar valores, usando as chaves, exemplos: ["A"], ["B"]

print(meu_dicionario) # → imprimi da forma declarada
"""
"""
for chave in meu_dicionario:
#   print(chave)
#   print(meu_dicionario[chave])
    print(chave+"-"+meu_dicionario[chave])
"""

# usando função items() retorna todos os items, e converte o dicionário em uma tupla => um conjunto de dados que são imutáveis => não pode ser mudado, alterado.

# for i in meu_dicionario.items():
    
# for i in meu_dicionario.values(): # → volta só os valores

    
for i in meu_dicionario.keys(): # → volta só as chaves
    
    
    print(i)