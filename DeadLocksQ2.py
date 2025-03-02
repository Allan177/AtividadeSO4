"""""
Uma solução eficiente para evitar deadlocks é garantir que todos os processos adquiram os recursos na mesma ordem.
Se todos os processos sempre tentarem pegar Recurso A antes de Recurso B, o impasse nunca ocorrerá. 
Todos os processos adquirem os recursos sempre na mesma ordem (Recurso A → Recurso B
"""

import threading
import time

# Criando dois recursos como locks
recurso_A = threading.Lock()
recurso_B = threading.Lock()

def processo(nome):
    print(f"{nome} tentando adquirir Recurso A")
    with recurso_A:  # Sempre pega o recurso A primeiro
        print(f"{nome} adquiriu Recurso A")
        time.sleep(1)

        print(f"{nome} tentando adquirir Recurso B")
        with recurso_B:  # Depois pega o recurso B
            print(f"{nome} adquiriu Recurso B")
            time.sleep(1)

    print(f"{nome} liberou os recursos")

# Criando as threads para simular os processos
t1 = threading.Thread(target=processo, args=("P1",))
t2 = threading.Thread(target=processo, args=("P2",))
t3 = threading.Thread(target=processo, args=("P3",))
t4 = threading.Thread(target=processo, args=("P4",))

# Iniciando os processos
t1.start()
t2.start()
t3.start()
t4.start()

# Aguardando a finalização dos processos
t1.join()
t2.join()
t3.join()
t4.join()
