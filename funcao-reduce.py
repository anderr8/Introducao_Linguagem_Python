# Python avançado função reduce => está função recebe uma lista e ela retorna um único valor.

from functools import reduce

def soma(x, y):
    return x+y

lista = [1, 3, 5, 10, 20]

soma = reduce(soma, lista)
print(soma)