"""
def soma(x, y):
    print(x+y)
    
soma(2, 3)
"""
# Exemplo 2:

def soma(x, y):
    return x+y

def multiplicacao(x, y):
    return x*y

s = soma(2, 3)
m = multiplicacao(3, 4)

print(s)
print(m)
print(soma(s, m))