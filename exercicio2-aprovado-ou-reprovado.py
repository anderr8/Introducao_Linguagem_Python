aluno = str(input("O nome do aluno: "))
print(aluno)

nota1 = float(input("Dígite a primeira nota: "))
nota2 = float(input("Dígite a segunda nota: "))

media = (nota1+nota2)/2

if media >= 6:
    print("O aluno ", aluno, "está APROVADO!")
else:
    print("O aluno", aluno, "Reprovado")