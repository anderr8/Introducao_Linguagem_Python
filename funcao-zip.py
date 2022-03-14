# Funçaõ zip → concatena listas, para mostrar os itens delas
# expected = esperado/a

lista1 = [1, 2, 3, 4, 5]
lista2 = ["abacate;", "bola;", "cachorro;", "dinheiro;", "elefante;"]
lista3 = ["R$ 2,00", "R$5,00", "R$100,00", "Cotação hoje R$3,55", "Não tem preço!"]

"""
for numero, nome in zip(lista1, lista2):
    print(numero, nome)
"""

for numero, nome, valor in zip(lista1, lista2, lista3):
    print(numero, nome, valor)