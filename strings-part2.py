# a = "Diego"
# b = "Mariano"

# \n -> caractere especial

# concatenar = a + " " + b + "\n"

"""
print(concatenar)
print(concatenar.lower()) # imprimi em minúscula
print(concatenar.upper()) # imprimi em Maiúscula

concatenar = concatenar.upper()
print(concatenar)
"""
# print(concatenar.strip()) # strip remove caracteres especiais e espaços

minha_string = "O rato roeu a roupa do rei de Roma"

"""
minha_lista = minha_string.split("r")
print(minha_lista)
"""
# case sensitive => é sensivel as letras maiúsculas e minúsculas

"""
busca = minha_string.find("rei") # comando para buscar string
print(minha_string[busca:]) # se não encontrar a string é retornado -1
"""

minha_string = minha_string.replace("do rei", "da rainha")
print(minha_string)