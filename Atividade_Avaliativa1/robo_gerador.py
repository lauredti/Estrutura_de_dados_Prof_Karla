import random

# Gerar lista unidimensional com valores aleatórios
def gerar_array(tamanho, limite_min=1, limite_max=10000):
    array = [random.randint(limite_min, limite_max) for _ in range(tamanho)]
    return array

# Gerar matriz bidimensional com valores aleatórios
def gerar_matriz(linhas, colunas, limite_min=1, limite_max=1000):
    matriz = []
    for _ in range(linhas):
        linha = [random.randint(limite_min, limite_max) for _ in range(colunas)]
        matriz.append(linha)
    return matriz