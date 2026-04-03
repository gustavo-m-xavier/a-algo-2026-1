def merge_sort(arr):
    """
    Implementação do algoritmo de ordenação Merge Sort, que tem complexidade O(n log n)

    Params: arr com a arr a ser ordenada
    Returns: arr ordenada
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    """
    Função auxiliar para o Merge Sort, que combina duas arrs ordenadas em uma única arr ordenada

    Params: left e right, as duas arrs ordenadas
    Returns: arr ordenada resultante da combinação de left e right
    """
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def multiplicar_matrizes(A, B):
    """
    Implementação da multiplicação de matrizes, que tem complexidade O(n^3)

    Params: A e B, as matrizes a serem multiplicadas
    Returns: matriz resultante da multiplicação de A e B
    """
    n = len(A)
    m = len(B[0])
    p = len(B)

    result = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            for k in range(p):
                result[i][j] += A[i][k] * B[k][j]

    return result


def main():
    """
    Função main para testar os algoritmos implementados e apresentar sua complexidade.
    """
    print("=== MERGE SORT ===")
    arr = [5, 2, 9, 1, 5, 6]
    print("Original:", arr)
    print("Ordenado:", merge_sort(arr))

    print("\n=== MATRIZES ===")
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    print("result:", multiplicar_matrizes(A, B))

if __name__ == "__main__":
    main()
    