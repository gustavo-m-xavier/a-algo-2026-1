class MaxHeap:
    """
    Implementação de uma Max Heap utilizando lista.

    A heap mantém o maior valor sempre na raiz.
    Sempre que um item é inserido ou removido,
    a estrutura completa da heap é exibida.
    """

    def __init__(self):
        """
        Inicializa uma heap vazia.
        """
        self.heap = []

    def parent_index(self, index):
        """
        Retorna o índice do nó pai.

        :param index: Índice do nó atual.
        :return: Índice do pai.
        """
        return (index - 1) // 2

    def left_child_index(self, index):
        """
        Retorna o índice do filho esquerdo.

        :param index: Índice do nó atual.
        :return: Índice do filho esquerdo.
        """
        return 2 * index + 1

    def right_child_index(self, index):
        """
        Retorna o índice do filho direito.

        :param index: Índice do nó atual.
        :return: Índice do filho direito.
        """
        return 2 * index + 2

    def swap(self, first_index, second_index):
        """
        Troca dois elementos de posição na heap.

        :param first_index: Índice do primeiro elemento.
        :param second_index: Índice do segundo elemento.
        """
        self.heap[first_index], self.heap[second_index] = (
            self.heap[second_index],
            self.heap[first_index],
        )

    def insert(self, value):
        """
        Insere um novo valor na heap.

        Após a inserção, reorganiza a estrutura
        para manter a propriedade da Max Heap.

        :param value: Valor numérico a ser inserido.
        """
        print(f"\n➕ Inserindo: {value}")

        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

        self.print_heap()

    def heapify_up(self, index):
        """
        Move um elemento para cima até restaurar
        a propriedade da heap.

        :param index: Índice do elemento inserido.
        """
        while index > 0:
            parent = self.parent_index(index)

            if self.heap[index] > self.heap[parent]:
                self.swap(index, parent)
                index = parent
            else:
                break

    def remove(self):
        """
        Remove e retorna o maior elemento da heap.

        Após a remoção, reorganiza a estrutura
        para manter a propriedade da Max Heap.

        :return: Maior valor da heap.
        """
        if not self.heap:
            print("\n⚠️ Heap vazia.")
            return None

        if len(self.heap) == 1:
            removed_value = self.heap.pop()

            print(f"\n➖ Removendo: {removed_value}")
            self.print_heap()

            return removed_value

        removed_value = self.heap[0]

        print(f"\n➖ Removendo: {removed_value}")

        self.heap[0] = self.heap.pop()
        self.heapify_down(0)

        self.print_heap()

        return removed_value

    def heapify_down(self, index):
        """
        Move um elemento para baixo até restaurar
        a propriedade da heap.

        :param index: Índice do elemento.
        """
        size = len(self.heap)

        while True:
            left = self.left_child_index(index)
            right = self.right_child_index(index)

            largest = index

            if left < size and self.heap[left] > self.heap[largest]:
                largest = left

            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != index:
                self.swap(index, largest)
                index = largest
            else:
                break

    def print_heap(self):
        """
        Exibe a estrutura atual da heap.
        """
        print("Heap atual:", self.heap)


# =========================
# Exemplo de uso
# =========================

heap = MaxHeap()

heap.insert(10)
heap.insert(4)
heap.insert(15)
heap.insert(20)
heap.insert(1)
heap.insert(8)

heap.remove()
heap.remove()
heap.remove()