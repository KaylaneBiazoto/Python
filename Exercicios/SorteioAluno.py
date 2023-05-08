from random import shuffle

n = int(input("Digite numero de alunos que deseja sortear: "))

aluno = []

for i in range(0, n):

    nome = str(input("{}° Aluno: ".format(i+1)))

    aluno.append(nome)

shuffle(aluno) # Embaralha, mudando a ordem.

print(f'A ordem de apresentação será {aluno}')