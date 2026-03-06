#versao normal
import time

def cronometro_interativo(n):
    print('Inicio')
    while n >= 0:
        print(n)
        time.sleep(1)
        n -= 1
    print('fim')
cronometro_interativo(10)

#versao recursiva

def cronometro_recursivo(n):
    #1 caso base: evita o loop infinito
    if (n < 0):
        print('fim')
        return
 #2ação que a função vai executar   
    print(n)
    time.sleep(1)
    cronometro_recursivo(n-1)

cronometro_recursivo(10)