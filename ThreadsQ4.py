import threading
import time

# Função para contar de 1 a 10
def contar():
    for i in range(1, 11):
        print(f'Contando: {i}')
        time.sleep(1)

# Função para imprimir letras de A a J
def imprimir_letras():
    for letra in 'ABCDEFGHIJ':
        print(f'Letra: {letra}')
        time.sleep(1)

# Criando as threads
thread_contar = threading.Thread(target=contar)
thread_imprimir = threading.Thread(target=imprimir_letras)

# Iniciando as threads
thread_contar.start()
thread_imprimir.start()

# Esperando as threads terminarem
thread_contar.join()
thread_imprimir.join()

print("Tarefas finalizadas!")
