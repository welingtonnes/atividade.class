import numpy as np

dieimes_matriz = np.array([[3, 4, 1], [3, 2, 1]])
soma_elementos = 0

for linha in dieimes_matriz:
    for elemento in linha:
        soma_elementos += elemento

print("A soma de todos os elementos da matriz é:", soma_elementos)