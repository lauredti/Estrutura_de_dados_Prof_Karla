
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
            for cenario in ["Aleatório", "Ordenado", "Invertido"]:
                print(f"\n--- Cenário: {cenario} ---")
                print(f"{'Tamanho':<8} | {'Bubble Comp.':<13} | {'Bubble T.':<13} | {'Quick Comp.':<13} | {'Quick T.':<13} | {'Insert Comp.':<13} | {'Insert T.':<13} | {'Select Comp.':<13} | {'Select T.':<13}")
                print("-" * 70)
            
                for tam in tamanhos:
                    base = gerar_array(tam)
                    if cenario == "Aleatório":
                        original = base
                    elif cenario == "Ordenado":
                        original = sorted(base)
                    else:
                        original = sorted(base, reverse=True)
                
                    _, b_comp, b_trocas = bubble_sort(original)
                    _, q_comp, q_mov = quick_sort(original)
                    _, i_comp, i_mov = insertion_sort(original)
                    _, s_comp, s_trocas = selection_sort(original)
                    print(f"{tam:<8} | {b_comp:<13} | {b_trocas:<13} | "
                f"{q_comp:<13} | {q_mov:<13} | "
                f"{i_comp:<13} | {i_mov:<13} | "
                f"{s_comp:<13} | {s_trocas:<13}")


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
            temperaturas = []
            print("\nDigite as 10 temperaturas:")
            for i in range(10):
                valor = float(input(f"Temperatura {i + 1}/10: "))
                temperaturas.append(valor)
        
            executar_hands_on_1(temperaturas)

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