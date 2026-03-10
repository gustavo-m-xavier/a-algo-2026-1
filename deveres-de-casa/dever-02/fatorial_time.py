import time
import sys

sys.setrecursionlimit(2000)


def fatorial(n):
    """
    Função recursiva que calcula o fatorial de um número n.
    
    Caso base:
        Se n for 0 ou 1, retorna 1.
    
    Caso recursivo:
        n! = n * (n-1)!
    """

    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


def get_time(n):
    """
    Mede o tempo de execução da função fatorial
    para um determinado valor de n.
    """

    inicio = time.perf_counter()  # início da medição
    
    resultado = fatorial(n)  # cálculo do fatorial
    
    fim = time.perf_counter()  # fim da medição

    tempo = fim - inicio

    print(f"n = {n}")
    print(f"Tempo de execução: {tempo:.10f} segundos")
    print("-" * 40)


def main():
    """
    Executa o algoritmo para diferentes valores de n.
    """

    valores = [10, 100, 500, 1000]

    print("Teste de desempenho do fatorial recursivo\n")

    for n in valores:
        get_time(n)


if __name__ == "__main__":
    main()