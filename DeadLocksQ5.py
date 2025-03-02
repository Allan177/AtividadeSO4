"""""
O algoritmo do avestruz é uma estratégia de gerenciamento de deadlock que simplesmente ignora o problema. 
Ele parte do princípio de que os deadlocks são raros, então gastar recursos para evitá-los pode ser menos eficiente 
do que simplesmente reiniciar o sistema se um deadlock ocorrer.
"""

import threading
import time

# Criando dois recursos como locks
recurso_A = threading.Lock()
recurso_B = threading.Lock()

def processo_avestruz(nome):
    print(f"{nome} tentando adquirir Recurso A")
    recurso_A.acquire()
    print(f"{nome} adquiriu Recurso A")
    time.sleep(1)

    print(f"{nome} tentando adquirir Recurso B")
    recurso_B.acquire()  # Se houver deadlock, ele nunca vai liberar os recursos
    print(f"{nome} adquiriu Recurso B")

    # Liberando recursos (nunca chegará aqui se houver deadlock)
    recurso_B.release()
    recurso_A.release()
    print(f"{nome} liberou os recursos")

# Criando as threads para simular os processos
t1 = threading.Thread(target=processo_avestruz, args=("P1",))
t2 = threading.Thread(target=processo_avestruz, args=("P2",))

# Iniciando os processos
t1.start()
t2.start()

# Aguardando a finalização dos processos (nunca vai terminar se houver deadlock)
t1.join()
t2.join()
