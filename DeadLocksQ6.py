"""""
O algoritmo impede o impasse, ao negar ou adiar o pedido se ele determinar que aceitar o pedido
pode colocar o sistema em um estado inseguro (onde um impasse poderia ocorrer).
"""

""""
coloque pip install numpy no terminal para baixer uma dependecia necessaria para rodar o codigo

"""



import numpy as np

class Banqueiro:
    def __init__(self, total_recursos, maximo, alocado):
        """Inicializa os recursos do sistema e os processos"""
        self.total_recursos = np.array(total_recursos)  # Recursos totais disponíveis
        self.maximo = np.array(maximo)  # Máximo que cada processo pode requisitar
        self.alocado = np.array(alocado)  # Recursos já alocados para cada processo
        self.necessario = self.maximo - self.alocado  # Recursos ainda necessários
        self.disponivel = self.total_recursos - np.sum(self.alocado, axis=0)  # Recursos disponíveis

    def estado_seguro(self):
        """Verifica se o sistema está em um estado seguro (sem risco de deadlock)"""
        trabalho = self.disponivel.copy()  # Recursos temporários para simulação
        finalizado = np.zeros(len(self.maximo), dtype=bool)  # Marca processos finalizados
        ordem_execucao = []

        while True:
            encontrado = False
            for i in range(len(self.maximo)):
                if not finalizado[i] and np.all(self.necessario[i] <= trabalho):
                    trabalho += self.alocado[i]  # Simula liberação de recursos
                    finalizado[i] = True
                    ordem_execucao.append(i)
                    encontrado = True

            if not encontrado:
                break  # Se nenhum processo puder ser executado, sair do loop

        if np.all(finalizado):
            return True, ordem_execucao  # Estado seguro encontrado
        else:
            return False, []  # Deadlock detectado

    def solicitar_recurso(self, processo, requisicao):
        """Processa uma requisição de recursos de um processo"""
        requisicao = np.array(requisicao)

        # Verifica se o processo está pedindo mais do que declarou como máximo
        if np.any(requisicao > self.necessario[processo]):
            print(f"❌ ERRO: Processo {processo} solicitou mais do que seu máximo declarado.")
            return False

        # Verifica se há recursos disponíveis
        if np.any(requisicao > self.disponivel):
            print(f"⚠️ Processo {processo} deve esperar, pois os recursos não estão disponíveis.")
            return False

        # Simula a alocação temporária
        self.disponivel -= requisicao
        self.alocado[processo] += requisicao
        self.necessario[processo] -= requisicao

        # Verifica se o sistema permanece seguro após a alocação
        seguro, ordem = self.estado_seguro()
        if seguro:
            print(f"✅ Pedido do Processo {processo} aprovado! Sistema ainda seguro.")
            return True
        else:
            print(f"🚨 Pedido do Processo {processo} negado! Estado inseguro detectado.")
            # Reverte a alocação se o estado não for seguro
            self.disponivel += requisicao
            self.alocado[processo] -= requisicao
            self.necessario[processo] += requisicao
            return False

# -----------------------------------
# 📌 Simulação de um Cenário
# -----------------------------------

# Definição dos recursos disponíveis no sistema
total_recursos = [10, 5, 7]  # 10 unidades do Recurso A, 5 do B, 7 do C

# Máximo que cada processo pode precisar
maximo = [
    [7, 5, 3],   # Processo 0
    [3, 2, 2],   # Processo 1
    [9, 0, 2]    # Processo 2
]

# Recursos atualmente alocados para cada processo
alocado = [
    [0, 1, 0],   # Processo 0 tem 0A, 1B, 0C
    [2, 0, 0],   # Processo 1 tem 2A, 0B, 0C
    [3, 0, 2]    # Processo 2 tem 3A, 0B, 2C
]

# Criando o sistema do Banqueiro
banco = Banqueiro(total_recursos, maximo, alocado)

# 🔄 Verificando o estado inicial
seguro, ordem = banco.estado_seguro()
if seguro:
    print(f"🔄 O sistema está seguro! Ordem segura de execução: {ordem}")
else:
    print("⚠️ O sistema está em um estado inseguro!")

# 🔹 Testando requisições de processos
print("\n🛠️ Testando solicitações de recursos:")

# Processo 1 tenta solicitar [1, 0, 2] recursos
banco.solicitar_recurso(1, [1, 0, 2])

# Processo 0 tenta solicitar [3, 3, 0] recursos
banco.solicitar_recurso(0, [3, 3, 0])

# Processo 2 tenta solicitar [6, 0, 0] recursos (deve ser negado)
banco.solicitar_recurso(2, [6, 0, 0])
