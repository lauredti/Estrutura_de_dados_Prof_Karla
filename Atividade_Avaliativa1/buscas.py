# Busca sequencial em matriz bidimensional
def busca_sequencial_matriz(matriz, valor_procurado):

    # 1. Obter dimensões da matriz
    linhas = len(matriz)
    colunas = len(matriz[0]) if linhas > 0 else 0

    # 2. Inicializar contador de comparações
    comparacoes = 0

    # 3. Percorrer linhas e colunas
    for i in range(linhas):
        for j in range(colunas):
            comparacoes += 1

            # Verificar se encontrou o valor
            if matriz[i][j] == valor_procurado:
                return True, i, j, comparacoes

    # 4. Caso não encontre o valor após varrer toda a matriz            
    return False, -1, -1, comparacoes