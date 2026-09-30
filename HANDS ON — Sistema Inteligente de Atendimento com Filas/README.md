

## Relatório e análise

#### 1. Por que a ordem de atendimento da fila de prioridade pode ser diferente da ordem da fila clássica?

*A fila clássica obedece ao critério FIFO , atendendo quem chegou mais cedo. Já a fila de prioridade reorganiza os elementos com base na gravidade ou importância do atendimento, fazendo com que clientes prioritários "furem a fila" de forma controlada, mesmo que tenham chegado muito tempo depois de clientes com atendimento normal.*


#### 2. Em quais situações reais uma fila de prioridade seria mais adequada?

*Triagem hospitalar, sistemas operacionais, roteamento de redes entre outros que sua prioridade seja importante para o processo.*

#### 3. Quais são as vantagens e limitações de uma fila circular?

* *Vantagens: Ocupa um bloco de memória fixo e pré-alocado, não necessita deslocar todos os elementos para a esquerda a cada remoção e permite reutilização contínua de memória via aritmética modular.*
* *Limitações: Capacidade máxima rígida. Se houver pico de demanda inesperado, ela não consegue expandir dinamicamente sem ser recriada ou realocada na memória.*

#### 4. O que acontece ao tentar inserir um elemento em uma fila circular cheia?


*Ocorre um erro de overflow. O algoritmo deve rejeitar a inserção para não sobrescrever dados pendentes ou, em implementações de substituição, sobrescrever o dado mais antigo que ainda não havia sido processado.*

