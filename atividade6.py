alunos = []  # Lista para armazenar os dados dos alunos

# Loop para ler os dados dos alunos
for i in range(3):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    alunos.append((nome, nota))  # Armazena o nome e a nota como uma tupla na lista

soma_notas = 0  # Variável para armazenar a soma das notas dos alunos

# Loop para somar as notas dos alunos
for aluno in alunos:
    soma_notas += aluno[1]  # Acessa a nota do aluno na posição 1 da tupla

media = soma_notas / len(alunos)  # Calcula a média das notas

print("A média das notas é:", media)
