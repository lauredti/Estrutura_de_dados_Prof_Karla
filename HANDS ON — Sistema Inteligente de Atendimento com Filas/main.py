import heapq
import random


class Cliente:
    def __init__(self, nome, senha, prioridade):
        self.nome = nome
        self.senha = senha
        self.prioridade = prioridade

    def __repr__(self):
        prioridades_str = {1: "Emergência", 2: "Prioritário", 3: "Normal"}
        return f"[{self.senha}] {self.nome} (Prioridade: {prioridades_str.get(self.prioridade, self.prioridade)})"


class Fila:
    def __init__(self):
        self.itens = []

    def enqueue(self, cliente):
        self.itens.append(cliente)

    def dequeue(self):
        if self.empty():
            return None
        return self.itens.pop(0)

    def head(self):
        if self.empty():
            return None
        return self.itens[0]

    def tamanho(self):
        return len(self.itens)

    def empty(self):
        return len(self.itens) == 0


class FilaCircular:
    def __init__(self, capacidade=5):
        self.capacidade = capacidade
        self.fila = [None] * capacidade
        self.frente = 0
        self.fim = 0
        self.total_itens = 0

    def _redimensionar(self, nova_capacidade):
        nova_fila = [None] * nova_capacidade
        for i in range(self.total_itens):
            indice_antigo = (self.frente + i) % self.capacidade
            nova_fila[i] = self.fila[indice_antigo]

        self.fila = nova_fila
        self.frente = 0
        self.fim = self.total_itens
        self.capacidade = nova_capacidade

    def cheio(self):
        return self.total_itens == self.capacidade

    def empty(self):
        return self.total_itens == 0

    def enqueue(self, cliente):
        if self.cheio():
            self._redimensionar(self.capacidade * 2)

        self.fila[self.fim] = cliente
        self.fim = (self.fim + 1) % self.capacidade
        self.total_itens += 1

    def dequeue(self):
        if self.empty():
            print("Erro: Fila circular vazia!")
            return None

        removido = self.fila[self.frente]
        self.fila[self.frente] = None
        self.frente = (self.frente + 1) % self.capacidade
        self.total_itens -= 1
        return removido

    def head(self):
        if self.empty():
            return None
        return self.fila[self.frente]

    def tamanho(self):
        return self.total_itens

    def mostrar_indices(self):
        print(f"Começo: {self.frente} | fim: {self.fim} | Ocupados: {self.total_itens}/{self.capacidade}")


class FilaPrioridade:
    def __init__(self):
        self.heap = []
        self.contador = 0

    def enqueue(self, cliente):
        heapq.heappush(self.heap, (cliente.prioridade, self.contador, cliente))
        self.contador += 1

    def dequeue(self):
        if self.empty():
            return None
        _, _, cliente = heapq.heappop(self.heap)
        return cliente

    def head(self):
        if self.empty():
            return None
        return self.heap[0][2]

    def tamanho(self):
        return len(self.heap)

    def empty(self):
        return len(self.heap) == 0


def menu_interativo():
    fila_selecionada = None
    print("\n--- Modo Interativo ---")
    print("1 - Fila Clássica")
    print("2 - Fila Circular")
    print("3 - Fila de Prioridade")
    opcao_fila = input("Escolha a fila que quer testar: ")

    if opcao_fila == "1":
        fila_selecionada = Fila()
    elif opcao_fila == "2":
        fila_selecionada = FilaCircular(5)
    elif opcao_fila == "3":
        fila_selecionada = FilaPrioridade()
    else:
        print("Opção inválida, voltando...")
        return

    contador_senha = 1
    while True:
        print("\n1. Inserir cliente")
        print("2. Atender cliente")
        print("3. Consultar próximo (head)")
        print("4. Mostrar tamanho/estado")
        print("0. Voltar ao menu principal")
        opcao = input("Opção: ")

        if opcao == "1":
            nome = input("Nome do cliente: ")
            prio = int(input("Prioridade (1-Emergência, 2-Prioritário, 3-Normal): "))
            c = Cliente(nome, f"SENHA-{contador_senha}", prio)
            contador_senha += 1
            fila_selecionada.enqueue(c)
            print(f"Inserido: {c}")
        elif opcao == "2":
            atendido = fila_selecionada.dequeue()
            print(f"Atendido: {atendido}" if atendido else "Ninguém para atender.")
        elif opcao == "3":
            proximo = fila_selecionada.head()
            print(f"Próximo da fila: {proximo}" if proximo else "Fila vazia.")
        elif opcao == "4":
            print(f"Tamanho atual: {fila_selecionada.tamanho()}")
            if isinstance(fila_selecionada, FilaCircular):
                fila_selecionada.mostrar_indices()
        elif opcao == "0":
            break
          
def simular_desafio():

    nomes_base = [
        "Ana", "Bruno", "Carlos", "Daniela", "Eduardo",
        "Fernanda", "Gabriel", "Helena", "Igor", "Juliana",
        "Lucas", "Mariana", "Nicolas", "Olivia", "Pedro",
        "Rafaela", "Samuel", "Tatiana", "Vinicius", "Yasmin"
    ]
    
    clientes = [
        Cliente(nome=nomes_base[i], senha=f"SENHA-{i+1:02d}", prioridade=random.randint(1, 3))
        for i in range(20)
    ]

    print("=" * 60)
    print("1. CLIENTES NA ORDEM DE CHEGADA")
    print("=" * 60)
    for c in clientes:
        print(c)


    fila_classica = Fila()
    for c in clientes:
        fila_classica.enqueue(c)

    print("\n" + "=" * 60)
    print("2. ORDEM DE ATENDIMENTO - FILA CLÁSSICA")
    print("=" * 60)
    atendidos_classica = []
    while not fila_classica.empty():
        atendido = fila_classica.dequeue()
        atendidos_classica.append(atendido)
        print(f"Atendido: {atendido}")

    fila_circ = FilaCircular(capacidade=5)
    print("\n" + "=" * 60)
    print("3. COMPORTAMENTO DA FILA CIRCULAR")
    print("=" * 60)
    print("-> Inserindo clientes e observando redimensionamento:")
    for c in clientes:
        fila_circ.enqueue(c)
        print(f"Inserido {c.senha} | Frente: {fila_circ.frente} | Fim: {fila_circ.fim} | Ocupados: {fila_circ.total_itens}/{fila_circ.capacidade}")

    print("\n-> Desenfileirando da Fila Circular:")
    atendidos_circ = []
    while not fila_circ.empty():
        atendido = fila_circ.dequeue()
        atendidos_circ.append(atendido)
        print(f"Atendido: {atendido} | Restantes: {fila_circ.total_itens}")

    fila_prio = FilaPrioridade()
    for c in clientes:
        fila_prio.enqueue(c)

    print("\n" + "=" * 60)
    print("4. ORDEM DE ATENDIMENTO - FILA DE PRIORIDADE")
    print("=" * 60)
    atendidos_prio = []
    while not fila_prio.empty():
        atendido = fila_prio.dequeue()
        atendidos_prio.append(atendido)
        print(f"Atendido: {atendido}")

    print("\n" + "=" * 60)
    print("5. COMPARAÇÃO DOS RESULTADOS OBTIDOS")
    print("=" * 60)
    print(f"{'Ordem':<6} | {'Fila Clássica':<30} | {'Fila Prioritária':<30}")
    print("-" * 72)
    for i in range(20):
        print(f"{i+1:02d}     | {str(atendidos_classica[i]):<30} | {str(atendidos_prio[i]):<30}")


if __name__ == "__main__":
    simular_desafio()

if __name__ == "__main__":
    menu_interativo()