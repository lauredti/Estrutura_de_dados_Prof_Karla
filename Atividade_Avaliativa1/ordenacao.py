# Algoritmo de ordenação Bubble Sort com contagem de métricas
def bubble_sort(lista_original):

    # 1. Criar cópia da lista e obter tamanho
    arr = list(lista_original)
    n = len(arr)

    # 2. Inicializar contadores
    comparacoes = 0
    trocas = 0

    # 3. Percorrer a lista com passadas sucessivas
    for i in range(n):
        houve_troca = False

        # 4. Comparar elementos adjacentes
        for j in range(0, n - i - 1):
            comparacoes += 1

            # Trocar elementos se estiverem fora de ordem
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocas += 1
                houve_troca = True

        # 5. Interromper antecipadamente se já estiver ordenado
        if not houve_troca:
            break

    # 6. Retornar array ordenado e métricas        
    return arr, comparacoes, trocas

# Algoritmo de ordenação Quick Sort (Divisão e Conquista)
def quick_sort(lista_original):

    # 1. Criar cópia da lista e métricas
    arr = list(lista_original)
    metricas = {"comparacoes": 0, "movimentacoes": 0}

    # 2. Função interna para particionamento
    def particionar(inicio, fim):
        pivo = arr[fim]
        i = inicio - 1

        # Percorrer sub-vetor comparando com o pivô
        for j in range(inicio, fim):
            metricas["comparacoes"] += 1
            if arr[j] <= pivo:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                metricas["movimentacoes"] += 1

        # Posicionar o pivô no índice correto        
        arr[i + 1], arr[fim] = arr[fim], arr[i + 1]
        metricas["movimentacoes"] += 1
        return i + 1

    # 3. Função recursiva do Quick Sort
    def quick_sort_recursivo(inicio, fim):
        if inicio < fim:
            indice_pivo = particionar(inicio, fim)
            quick_sort_recursivo(inicio, indice_pivo - 1)
            quick_sort_recursivo(indice_pivo + 1, fim)

    # 4. Executar ordenação completa
    quick_sort_recursivo(0, len(arr) - 1)

    # 5. Retornar resultado e métricas
    return arr, metricas["comparacoes"], metricas["movimentacoes"]