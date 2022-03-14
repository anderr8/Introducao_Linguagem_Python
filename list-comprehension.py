# Python avançado list comprehension = compreensão de lista

x = [1, 2, 3, 4, 5]
# y = [valor_a_adicionar laço condição] # isto é o que precisa ser adicionado.

y = [i**2 for i in x] # i**2 → valor_ a_adicionar, for i in x => laço 
z = [i for i in x if i%2==1] # if i%2==1 → condição buscar só os números ímpares

"""
for i in x:
    y.append(i**2) # forma mais simples de list comprehension


"""   
print("Usando list comprehension")
print(z)
print(x)
print(y)


