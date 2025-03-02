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

# Função para imprimir números ímpares de 1 a 10
def imprimir_impares():
    for i in range(1, 11, 2):
        print(f'Ímpar: {i}')
        time.sleep(1)

# Função para imprimir os quadrados de 1 a 5
def imprimir_quadrados():
    for i in range(1, 6):
        print(f'Quadrado de {i}: {i**2}')
        time.sleep(1)

# Criando as threads
thread_contar = threading.Thread(target=contar)
thread_imprimir_letras = threading.Thread(target=imprimir_letras)
thread_imprimir_impares = threading.Thread(target=imprimir_impares)
thread_imprimir_quadrados = threading.Thread(target=imprimir_quadrados)

# Iniciando as threads
thread_contar.start()
thread_imprimir_letras.start()
thread_imprimir_impares.start()
thread_imprimir_quadrados.start()

# Esperando as threads terminarem
thread_contar.join()
thread_imprimir_letras.join()
thread_imprimir_impares.join()
thread_imprimir_quadrados.join()

print("Tarefas finalizadas!")
