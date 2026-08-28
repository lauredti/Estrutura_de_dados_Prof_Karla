def bubble_sort(lista_original):
    arr = list(lista_original)
    n = len(arr)
    comparacoes = 0
    trocas = 0
    
    for i in range(n):
        houve_troca = False
        for j in range(0, n - i - 1):
            comparacoes += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocas += 1
                houve_troca = True
        if not houve_troca:
            break
            
    return arr, comparacoes, trocas

def quick_sort(lista_original):
    arr = list(lista_original)
    metricas = {"comparacoes": 0, "movimentacoes": 0}
    
    def particionar(inicio, fim):
        pivo = arr[fim]
        i = inicio - 1
        
        for j in range(inicio, fim):
            metricas["comparacoes"] += 1
            if arr[j] <= pivo:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                metricas["movimentacoes"] += 1
                
        arr[i + 1], arr[fim] = arr[fim], arr[i + 1]
        metricas["movimentacoes"] += 1
        return i + 1

    def quick_sort_recursivo(inicio, fim):
        if inicio < fim:
            indice_pivo = particionar(inicio, fim)
            quick_sort_recursivo(inicio, indice_pivo - 1)
            quick_sort_recursivo(indice_pivo + 1, fim)

    quick_sort_recursivo(0, len(arr) - 1)
    return arr, metricas["comparacoes"], metricas["movimentacoes"]