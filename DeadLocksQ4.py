from collections import defaultdict

class GrafoDeadlock:
    def __init__(self):
        self.grafo = defaultdict(list)

    def adicionar_aresta(self, origem, destino):
        """ Adiciona uma aresta de origem para destino no grafo """
        self.grafo[origem].append(destino)

    def detectar_ciclo(self):
        """ Detecta se há um ciclo no grafo (indicando deadlock) """
        visitado = set()
        pilha_recursiva = set()

        def dfs(no):
            if no in pilha_recursiva:
                return True  # Se o nó já está na pilha, há um ciclo
            if no in visitado:
                return False  # Nó já processado, não precisa verificar

            # Marcar como visitado e adicionar à pilha de recursão
            visitado.add(no)
            pilha_recursiva.add(no)

            for vizinho in self.grafo[no]:
                if dfs(vizinho):  # Se um ciclo for encontrado
                    return True

            pilha_recursiva.remove(no)  # Remover da pilha ao sair da recursão
            return False

        # Testar ciclos em todos os nós do grafo
        for no in self.grafo:
            if no not in visitado:
                if dfs(no):
                    return True  # Encontrado ciclo (deadlock)

        return False  # Sem ciclos → Sem deadlock


# Criando um grafo que representa alocação de recursos
grafo = GrafoDeadlock()


grafo.adicionar_aresta("P1", "R1")
grafo.adicionar_aresta("R1", "P2")
grafo.adicionar_aresta("P2", "R2")
grafo.adicionar_aresta("R2", "P1")  # Causa o deadlock

# Detectando deadlock
if grafo.detectar_ciclo():
    print("⚠️ Deadlock detectado!")
else:
    print("✅ Nenhum deadlock encontrado.")
