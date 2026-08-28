import random

def gerar_array(tamanho, limite_min=1, limite_max=10000):
    array = [random.randint(limite_min, limite_max) for _ in range(tamanho)]
    return array

def gerar_matriz(linhas, colunas, limite_min=1, limite_max=1000):
    matriz = []
    for _ in range(linhas):
        linha = [random.randint(limite_min, limite_max) for _ in range(colunas)]
        matriz.append(linha)
    return matriz