
from robo_gerador import gerar_array, gerar_matriz
from ordenacao import bubble_sort, quick_sort
from buscas import busca_sequencial_matriz
from hands_on import executar_hands_on_1, executar_hands_on_2
import random

# Menu interativo
def menu_principal():
    while True:
        # 1. Exibir opções do menu
        print(" \n --- MENU --- \n ")
        print("1. Experimento de Ordenação (Bubble vs Quick)")
        print("2. Busca em Matrizes")
        print("3. Hands On 1 - Análise de temperatura")
        print("4. Hands On 2 - Monitoramento de Sensores")
        print("0. Sair")

        # 2. Ler opção do usuário
        opcao = input("\nEscolha uma opção: ")

        # 3. Executar opção 1 - Experimento de ordenação
        if opcao == "1":
            print("\nExecutando o experimento com listas de 10, 20 e 1000 elementos...\n")
            tamanhos = [10, 20, 1000]
            print(f"{'Tamanho':<10} | {'Bubble Comparação':<10} | {'Bubble Trocas':<14} | {'Quick Comparação':<10} | {'Quick Movimentações':<10}")
            print("-" * 70)
            
            for tam in tamanhos:
                original = gerar_array(tam)
                _, b_comp, b_trocas = bubble_sort(original)
                _, q_comp, q_mov = quick_sort(original)
                print(f"{tam:<10} | {b_comp:<17} | {b_trocas:<14} | {q_comp:<16} | {q_mov:<10}")

        # 4. Executar opção 2 - Busca em matriz       
        elif opcao == "2":
            print("\nBusca em Matriz Personalizada")
            
            linhas = int(input("Quantidade de linhas: "))
            colunas = int(input("Quantidade de colunas: "))
            
            matriz = gerar_matriz(linhas, colunas, 1, 100)
            
            print("\nMatriz gerada:")
            for linha in matriz:
                print("  ".join(f"{num:3}" for num in linha))
                
            alvo = int(input("\nDigite o número que você quer buscar: "))
            
            encontrado, lin, col, comparacoes = busca_sequencial_matriz(matriz, alvo)
            
            if encontrado:
                print(f"\nValor {alvo} encontrado na posição: Linha {lin}, Coluna {col}")
            else:
                print(f"\nValor {alvo} não encontrado na matriz.")
                
            print(f"Total de comparações feitas: {comparacoes}")

        # 5. Executar opção 3 - Hands On 1                
        elif opcao == "3":
            temperaturas_teste = [19.5, 21.0, 18.2, 25.3, 16.7, 22.4, 20.1, 27.8, 17.2, 23.6]
            executar_hands_on_1(temperaturas_teste)

        # 6. Executar opção 4 - Hands On 2   
        elif opcao == "4":
            matriz_sensores = [[round(random.uniform(15.0, 35.0), 1) for _ in range(24)] for _ in range(5)]
            try:
                limite = float(input("Informe o limite de temperatura para alerta (ex: 28.0): "))
            except ValueError:
                limite = 28.0
            executar_hands_on_2(matriz_sensores, limite)

        # 7. Encerrar o programa    
        elif opcao == "0":
            print("Encerrando o programa.")
            break

        # 8. Tratar opção inválida
        else:
            print("Opção invalida. Tente novamente.")

# Ponto de entrada do script
if __name__ == "__main__":
    menu_principal()