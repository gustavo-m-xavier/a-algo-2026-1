import random
import time

def insertion_sort(array, length) -> None:
    """
    Algoritmo de Insertion Sort para ordenar uma lista.

    Percorre o array a partir do segundo elemento e insere cada item
    na posição correta dentro da parte já ordenada.

    Params
    ----------
    array : list
        Lista de elementos a serem ordenados.
    length : int
        Tamanho da lista.

    Returns
    -------
    None
        A ordenação é feita in-place, modificando a lista original.
    """
    for i in range(1, length):
        chave = array[i]
        j = i - 1
        while j >= 0 and array[j] > chave:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = chave


def main() -> None:
    """
    Executa testes de desempenho comparando o Insertion Sort
    com o método embutido sorted() do Python.

    Gera listas aleatórias de diferentes tamanhos, mede o tempo
    de execução de cada algoritmo e imprime os resultados.

    Params
    ----------
    None

    Returns
    -------
    None
        Apenas imprime os tempos de execução no console.
    """
    tamanhos = [1000, 5000, 10000, 20000, 50000]

    for n in tamanhos:
        lista = [random.randint(0, 1000000) for _ in range(n)]

        lista_insertion = lista[:]
        lista_sorted = lista[:]

        inicio = time.time()
        insertion_sort(lista_insertion, len(lista_insertion))
        fim = time.time()
        tempo_insertion = fim - inicio

        inicio = time.time()
        lista_sorted = sorted(lista_sorted)
        fim = time.time()
        tempo_sorted = fim - inicio

        print(
            f"Tamanho {n:6d} | InsertionSort = {tempo_insertion:.4f}s "
            f"| sorted() = {tempo_sorted:.4f}s"
        )


if __name__ == "__main__":
    main()
