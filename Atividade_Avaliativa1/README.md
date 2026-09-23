## BUBBLE SORT, QUICK SORT, INSERT SORT E SELECT SORT

### Bubble Sort 
* O Bubble Sort é um tipo de algoritmo simples que organiza um conjunto de números, ele compara os números lado a lado e os troca de lugar conforme a sua ordem. Ele é eficaz em organizar listas pequenas, mas faz muito esforço em listas maiores. Em cada passagem, o maior elemento restante "flutua" até a sua posição final no final da lista.

* **Complexidade:**
  * Melhor caso: O(n) — ocorre quando a lista já está ordenada;
  * Caso médio: O(n²) — comparações e trocas frequentes em dados aleatórios;
  * Pior caso: O(n²) — ocorre quando a lista está em ordem totalmente inversa.
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
  * Pior caso: O(n²) — ocorre quando o pivô escolhido é sempre o menor ou o maior elemento.
* **Vantagens:**
  * Extremamente rápido na prática no caso médio.
  * Ordenação com baixo consumo de memória extra.
  * Excelente aproveitamento da memória cache do processador.
* **Limitações:**
  * Não é um algoritmo estável por padrão.
  * Pode atingir O(n²) se a escolha do pivô for ruim.
  * Implementação recursiva um pouco mais complexa.

* **Situações de uso:**
  * Adequado: Grandes volumes de dados em geral, bibliotecas padrão de linguagens e cenários onde velocidade média é prioridade.
  * Não é recomendado: Quando a estabilidade da ordenação é obrigatória, em sistemas de tempo real estrito com risco de O(n²), ou quando a estrutura de dados for uma lista encadeada.

### Insert Sort
O Insertion Sort funciona de forma semelhante a ordenar cartas de baralho na mão. Ele percorre a lista da esquerda para a direita, pegando um elemento por vez e inserindo-o na posição correta entre os elementos que já foram ordenados anteriormente.

* **Complexidade:**

  * Melhor caso:O(n)

  * Caso médio:O(n²)

  * Pior caso:O(n²)

* **Vantagens:**
  * Muito eficiente para conjuntos pequenos ou para listas que já estão quase ordenadas.
  * É um algoritmo estável.
  * Funciona bem como algoritmo online.
  * Não exige memória extra.
 
* **Limitações:**
  * Muito lento para listas grandes.Desempenho cai bastante com volumes grandes de dados no caso médio e no pior caso.
  * Realiza muitos deslocamentos/trocas quando os elementos menores estão muito próximos do final da lista.
 
* **Situações de uso:**

  * Adequado: Listas pequenas, dados quase ordenados ou fluxos contínuos de dados que chegam um a um.

  * Não é recomendado: Grandes volumes de dados desordenados ou invertidos.

### Select Sort
O Selection Sort percorre a lista procurando o menor elemento e o coloca na primeira posição. Depois, procura o segundo menor e coloca na segunda, repetindo o processo para o restante da lista até que tudo esteja ordenado.

* **Complexidade:**

  * Melhor caso:O(n²)

  * Caso médio:O(n²)

  * Pior caso:O(n²)

* **Vantagens:**
  * Simples de entender e implementar.
  * Realiza poucas trocas de posição na memória, o que ajuda se a operação de escrita for cara.
  * Não precisa de memória extra.
 
* **Limitações:**
  * Muito lento para listas grandes.
  * Compara os itens o tempo todo, mesmo que o vetor já esteja parcialmente ou totalmente ordenado.
  * Em sua implementação padrão, não é estável.
 
* **Situações de uso:**

  * Adequado: Pequenos conjuntos de dados onde o custo de gravar na memória é alto e a memória disponível é extremamente limitada.

  * Não é recomendado: Listas médias ou grandes, ou situações em que o desempenho geral do tempo de execução é importante. 

### Tabela Comparativa

| Característica | Bubble Sort | Quick Sort | Insert Sort | Select Sort
| :--- | :--- | :--- |:--- |:--- 
| **Princípio de funcionamento** | Compara pares adjacentes e troca-os se estiverem fora de ordem, fazendo os maiores valores "flutuarem" até o final. | Usa divisão e conquista: escolhe um pivô, particiona os dados (menores à esquerda, maiores à direita) e ordena recursivamente. | Constrói a lista ordenada elemento a elemento, inserindo cada novo item na posição correta entre os já ordenados. | Percorre a lista para encontrar o menor elemento restante e troca-o diretamente com o elemento da primeira posição não ordenada.
| **Melhor caso** | O(n) | O(n log n) | O(n) | O(n²)
| **Caso médio** | O(n²) | O(n log n) | O(n²) | O(n²)
| **Pior caso** | O(n²)| O(n²) | O(n²) | O(n²)
| **Uso de memória** | O(1)  | O(log n) | O(1) |O(1)
| **Vantagem principal** | Simplicidade conceitual e facilidade de código | Alta performance e escalabilidade para grandes dados | Extremamente eficiente para listas quase ordenadas ou pequenas, e é estável. | Minimiza o número de trocas.
| **Limitação principal** | Baixo desempenho em listas médias e grandes devido ao excesso de trocas. | Instável e suscetível ao pior caso O(n²) se o pivô for mal escolhido. | Lento para listas grandes e inversamente ordenadas devido a muitos deslocamentos. | Realiza sempre O(n²) comparações, mesmo que a lista já esteja totalmente ordenada.
| **Aplicação recomendada** | Fins educacionais ou conjuntos de dados minúsculos e quase ordenados. | Ordenação geral de grandes volumes de dados e bibliotecas padrão de sistemas. | Pequenas coleções de dados, listas que recebem novos dados continuamente ou dados quase ordenados. | Sistemas onde a escrita na memória é muito dispendiosa, já que reduz o número de trocas.

---

## EXPERIMENTO DE ORDENAÇÃO

a) Qual algoritmo realizou menos operações para 10 elementos?
* O Insertion Sort, com 28 comparações.

b) Qual algoritmo realizou menos trocas ou movimentações?
   * O Selection Sort realizou menos trocas: 5 trocas para tamanho 10, 16 para 20 e 994 para 1.000.
c) O comportamento observado para 10 elementos permaneceu semelhante quando o tamanho aumentou para 20?
  * Sim, em geral. O Quick Sort continuou liderando em eficiência geral com o menor número de comparações, o Selection Sort manteve o menor número de trocas, e tanto Bubble quanto Insertion continuaram exibindo crescimento acelerado.

d) O que aconteceu com a quantidade de operações quando o vetor passou para 1.000 elementos?
  * A quantidade de operações explodiu nos algoritmos quadráticos. O número de comparações do Bubble Sort e do Selection Sort saltou para quase 500 mil, enquanto o Insertion Sort ficou em torno de 254 mil comparações e trocas. Em contraste, o Quick Sort manteve um volume muito inferior.

e) Bubble Sort, Insertion Sort e Selection Sort apresentam complexidade O(n²) em situações típicas estudadas. Eles apresentaram exatamente a mesma quantidade de operações? Explique utilizando seus resultados.
  * Não. Ter a mesma classe assintótica O(n²) significa ter uma taxa de crescimento semelhante, mas não valores idênticos.

f) Qual algoritmo apresentou maior crescimento no número de operações?
  * O Bubble Sort e o Insertion Sort somando todas as operações.

g) Como o comportamento experimental do Quick Sort se diferenciou dos demais algoritmos?
  * Ele cresceu de forma muito mais suave e escalável. Enquanto os outros três algoritmos foram para centenas de milhares de operações em 1.000 elementos, o Quick Sort fez apenas 11.758 comparações e 5.619 trocas.

h) Os resultados encontrados são coerentes com as complexidades teóricas estudadas?
  * Sim. Para Bubble, Selection e Insertion, o número de comparações e trocas aumentou numa proporção quadrática enquanto o Quick Sort seguiu a complexidade média teórica de O(n log n).

i) Se você fosse responsável pelo sistema da central de distribuição e precisasse ordenar milhares de pedidos, qual dos quatro algoritmos escolheria? Justifique utilizando os resultados do experimento.
  * O Quick Sort. Na prática com 1.000 itens ele já executou cerca de 40 a 60 vezes menos operações no total que qualquer um dos outros três.

A organização inicial dos dados interfere na quantidade de operações realizadas por todos os algoritmos da mesma maneira?
  *   Não. Enquanto alguns se beneficiam muito quando a lista já está ordenada, como o Bubble Sort e o Insertion Sort, que reduzem bastante o número de comparações, outros, como o Selection Sort, mantêm exatamente a mesma quantidade de comparações em qualquer cenário.
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

---
## CONCLUSÃO
1. O aumento do tamanho da estrutura de dados influencia a quantidade de operações?
  * Sim. Quanto maior a quantidade de elementos (n), maior é o volume de trocas que o algoritmo precisa executar para processar ou ordenar os dados.

2. Bubble Sort e Quick Sort crescem da mesma maneira quando o número de elementos aumenta?
  * Não. Eles têm taxas de crescimento bem diferentes, o Bubble Sort tem crescimento quadrático, O(n²). Se o tamanho da lista dobra, a quantidade de operações chega a quadruplicar. Já o Quick Sort, tem crescimento linear-logarítmico na média, O(n log n). Ele escala de forma muito mais eficiente e processa grandes volumes de dados bem mais rápido.
3. Por que analisar somente o resultado final da ordenação não é suficiente para comparar algoritmos?
  * Porque o resultado final sempre será o mesmo a lista ordenada. O que define a qualidade e a escolha do algoritmo é o custo do processo para chegar lá, o que inclui:Tempo de execução, quantidade de trocas, comparações feitas, Uso de memória auxiliar e Estabilidade.