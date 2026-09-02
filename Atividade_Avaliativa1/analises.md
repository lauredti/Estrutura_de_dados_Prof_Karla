## BUBBLE SORT E QUICK SORT

### Bubble Sort 
* O Bubble Sort é um tipo de algoritmo simples que organiza um conjunto de números, ele compara os números lado a lado e os troca de lugar conforme a sua ordem. Ele é eficaz em organizar listas pequenas, mas faz muito esforço em listas maiores. Em cada passagem, o maior elemento restante "flutua" até a sua posição final no final da lista.

* **Complexidade:**
  * Melhor caso: O(n) — ocorre quando a lista já está ordenada;
  * Caso médio: O(n^2) — comparações e trocas frequentes em dados aleatórios;
  * Pior caso: O(n^2) — ocorre quando a lista está em ordem totalmente inversa.
* **Vantagens:**
  * Muito simples de entender e implementar;
  * É estável;
  * Não exige memória extra.
* **Limitações:**
  * Extremamente ineficiente para listas médias e grandes;
  * Executa um número excessivo de operações de troca.

* **Situações de uso:** 
  * Adequado: didática ou quando a lista tem pouquíssimos elementos e quase já está ordenada.
  * Não recomendado: Praticamente qualquer aplicação real, sistemas em produção ou grandes volumes de dados.


### Quick Sort 
* O Quick Sort é um algoritmo de  ordenar que utiliza a estratégia de “dividir e conquistar”. Ele escolhe um elemento como pivô, reorganiza os dados para que os valores menores fiquem à esquerda e os maiores à direita, e repete o processo até organizar. 

* **Complexidade:**
  * Melhor caso: O(n log n) — ocorre quando o pivô escolhido divide a lista exatamente ao meio a cada passo.
  * Caso médio: O(n log n) — divisão balanceada na maioria das listas desordenadas.
  * Pior caso: O(n^2) — ocorre quando o pivô escolhido é sempre o menor ou o maior elemento.
* **Vantagens:**
  * Extremamente rápido na prática no caso médio.
  * Ordenação com baixo consumo de memória extra.
  * Excelente aproveitamento da memória cache do processador.
* **Limitações:**
  * Não é um algoritmo estável por padrão.
  * Pode atingir O(n^2) se a escolha do pivô for ruim.
  * Implementação recursiva um pouco mais complexa.

* **Situações de uso:**
  * Adequado: Grandes volumes de dados em geral, bibliotecas padrão de linguagens e cenários onde velocidade média é prioridade.
  * Não é recomendado: Quando a estabilidade da ordenação é obrigatória, em sistemas de tempo real estrito com risco de O(n^2), ou quando a estrutura de dados for uma lista encadeada.


### Tabela Comparativa

| Característica | Bubble Sort | Quick Sort |
| :--- | :--- | :--- |
| **Princípio de funcionamento** | Compara pares adjacentes e troca-os se estiverem fora de ordem, fazendo os maiores valores "flutuarem" até o final. | Usa divisão e conquista: escolhe um pivô, particiona os dados (menores à esquerda, maiores à direita) e ordena recursivamente. |
| **Melhor caso** | O(n) | O(n log n) |
| **Caso médio** | O(n^2) | O(n log n) |
| **Pior caso** | O(n^2)| O(n^2) |
| **Uso de memória** | O(1)  | O(log n) |
| **Vantagem principal** | Simplicidade conceitual e facilidade de código | Alta performance e escalabilidade para grandes dados |
| **Limitação principal** | Baixo desempenho em listas médias e grandes devido ao excesso de trocas. | Instável e suscetível ao pior caso O(n^2) se o pivô for mal escolhido. |
| **Aplicação recomendada** | Fins educacionais ou conjuntos de dados minúsculos e quase ordenados. | Ordenação geral de grandes volumes de dados e bibliotecas padrão de sistemas. |

---

## EXPERIMENTO DE ORDENAÇÃO

a) Qual algoritmo realizou menos operações para 10 elementos?
* Quick Sort. Ele teve menos comparações e menos trocas.

b) O comportamento permaneceu igual para 20 elementos?
* Sim. O Quick Sort continuou bem mais eficiente que o Bubble Sort tanto em comparações quanto em trocas.

c) O que aconteceu quando o tamanho aumentou para 1.000 elementos?
* A diferença aumentou bastante. O Bubble Sort explodiu para quase 500 mil comparações e 250 mil trocas, enquanto o Quick Sort se manteve econômico, com apenas cerca de 11 mil comparações e 6 mil movimentações.

d) Qual algoritmo apresentou maior crescimento da quantidade de operações?
* Bubble Sort. O número de operações dele subiu em um ritmo muito mais acelerado conforme a entrada aumentou.

e) Os resultados experimentais são coerentes com as complexidades teóricas estudadas?
* Sim, o Bubble Sort compara praticamente todo mundo com todo mundo. Quando você coloca 1.000 itens, o esforço multiplica por ele mesmo, dando quase 500 mil comparações na tabela. Já o Quick Sort vai dividindo a lista no meio para resolver mais rápido. Para esses mesmos 1.000 itens, a matemática prevê algo em torno de 10 mil comparações, que bate certinho com as 11 mil que você mediu.

f) Em qual situação você escolheria Bubble Sort?
* Apenas para fins educativos ou para listas minúsculas onde a facilidade de escrever o código importa mais que a velocidade.

g) Em qual situação você escolheria Quick Sort?
 * Para listas médias e grandes na prática, sempre que você precisar de alta velocidade e bom uso de memória em situações do mundo real.

 ---
 ## INVESTIGAÇÃO DE BUSCA EM MATRIZES

a) Por que encontrar um elemento no início exige menos operações?
* Porque o algoritmo para assim que encontra o elemento. Como ele começa checando pela primeira posição [0][0], basta realizar 1 comparação para encerrar o processo.

b) O que acontece quando o elemento procurado não existe?
* O algoritmo percorre todas as linhas e todas as colunas até o fim. Ele testa cada uma das posições para ter certeza de que o item não está lá, atingindo o número máximo possível de comparações.

c) Qual é o pior caso da busca sequencial?
* O pior caso acontece quando o elemento procurado está na última posição da matriz ou não existe. Nas duas situações, o algoritmo é forçado a conferir todos os elementos.

d) Como o aumento das dimensões da matriz influencia a quantidade de operações?
* Aumenta de forma linear em relação ao total de itens. Se você multiplica a quantidade de células por 100, o pior caso de comparações também é multiplicado por 100.

e) Qual a complexidade da busca sequencial em uma matriz com m linhas e n colunas? 
* A complexidade de tempo é O(mXn), onde 'm' é a quantidade de linhas e 'n' é a quantidade de colunas.

---

## HANDS ON 1: INVESTIGAÇÃO DO ARRAY

A complexidade de tempo do algoritmo é linear, representada por O(n), onde 'n' é o tamanho do array. Isso acontece porque usa-se apenas laços simples que percorrem a lista do início ao fim de forma sequencial — primeiro para imprimir, depois para encontrar maior/menor/soma, e por fim para contar quem está acima da média —, sem nenhum laço aninhados. Assim, se o array crescer, a quantidade de operações vai aumentar na mesma proporção direta do número de elementos, mantendo também uma complexidade de espaço O(1).

---

## HANDS ON 2: MATRIZ APLICADA – MONITORAMENTO DE SENSORES

a) Por que são necessários loops aninhados;
* Como a matriz é uma estrutura bidimensional, um único laço só consegue avançar em uma dimensão por vez . Para varrer a tabela inteira, o laço externo fixa uma linha enquanto o laço interno percorre todas as colunas daquela linha antes de passar para a próxima.
b) Qual o papel dos índices [ i ][ j ];
* Funcionam como coordenadas dentro da matriz, sendo [ i ] as linhas e [ j ] as colunas.

c) Quantas posições da matriz são percorridas;

* 120 posições.

d) Qual a relação entre o número de linhas, colunas e quantidade de operações.

* A relação é multiplicativa: Total de iterações = Linhas X Colunas. Com 5 linhas e 24 colunas, o corpo do laço interno roda 5 X 24 = 120 vezes. Se o tamanho de qualquer dimensão mudar, o total de verificações cresce proporcionalmente ao produto das duas (complexidade O(L X C)).