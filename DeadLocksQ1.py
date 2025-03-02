import threading
import time

# Criando dois recursos como locks
recurso_A = threading.Lock()
recurso_B = threading.Lock()

def processo_1():
    print("P1 tentando adquirir Recurso A")
    recurso_A.acquire()
    print("P1 adquiriu Recurso A")
    time.sleep(1)  # Simula um atraso

    print("P1 tentando adquirir Recurso B")
    recurso_B.acquire()
    print("P1 adquiriu Recurso B")

    # Liberando recursos
    recurso_B.release()
    recurso_A.release()

def processo_2():
    print("P2 tentando adquirir Recurso B")
    recurso_B.acquire()
    print("P2 adquiriu Recurso B")
    time.sleep(1)

    print("P2 tentando adquirir Recurso A")
    recurso_A.acquire()
    print("P2 adquiriu Recurso A")

    recurso_A.release()
    recurso_B.release()

def processo_3():
    print("P3 tentando adquirir Recurso A")
    recurso_A.acquire()
    print("P3 adquiriu Recurso A")
    time.sleep(1)

    print("P3 tentando adquirir Recurso B")
    recurso_B.acquire()
    print("P3 adquiriu Recurso B")

    recurso_B.release()
    recurso_A.release()

def processo_4():
    print("P4 tentando adquirir Recurso B")
    recurso_B.acquire()
    print("P4 adquiriu Recurso B")
    time.sleep(1)

    print("P4 tentando adquirir Recurso A")
    recurso_A.acquire()
    print("P4 adquiriu Recurso A")

    recurso_A.release()
    recurso_B.release()

# Criando as threads para simular os processos
t1 = threading.Thread(target=processo_1)
t2 = threading.Thread(target=processo_2)
t3 = threading.Thread(target=processo_3)
t4 = threading.Thread(target=processo_4)

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
