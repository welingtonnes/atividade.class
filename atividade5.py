numeros = []  # Lista vazia para armazenar os números

# Loop para ler e armazenar os números
for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

soma = 0  # Variável para armazenar a soma dos números

# Loop para somar os valores digitados
for numero in numeros:
    soma += numero

print("A soma dos números é:", soma)
