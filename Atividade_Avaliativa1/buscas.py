def busca_sequencial_matriz(matriz, valor_procurado):
    linhas = len(matriz)
    colunas = len(matriz[0]) if linhas > 0 else 0
    comparacoes = 0
    
    for i in range(linhas):
        for j in range(colunas):
            comparacoes += 1
            if matriz[i][j] == valor_procurado:
                return True, i, j, comparacoes
                
    return False, -1, -1, comparacoes