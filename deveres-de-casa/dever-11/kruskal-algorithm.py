import time


class Graph:
    """
    Classe responsável por representar um grafo
    utilizando lista de arestas.
    """

    def __init__(self, vertices):
        """
        Inicializa o grafo.

        :param vertices: Quantidade de vértices.
        """
        self.v = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        """
        Adiciona uma aresta ao grafo.

        :param u: Nó de origem.
        :param v: Nó de destino.
        :param w: Peso da aresta.
        """
        self.graph.append([u, v, w])

    def find_root(self, parent, i):
        """
        Busca a raiz de um conjunto.

        :param parent: Lista de pais.
        :param i: Nó atual.

        :return: Raiz do conjunto.
        """
        if parent[i] == i:
            return i

        parent[i] = self.find_root(parent, parent[i])

        return parent[i]

    def union_sets(self, parent, rank, x, y):
        """
        Une dois conjuntos.

        :param parent: Lista de pais.
        :param rank: Lista de ranks.
        :param x: Primeiro conjunto.
        :param y: Segundo conjunto.
        """
        root_x = self.find_root(parent, x)
        root_y = self.find_root(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y

        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x

        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def execute_maximum_kruskal(self):
        """
        Executa o algoritmo de Kruskal
        para gerar a Árvore Geradora Máxima.

        :return:
            - Lista de arestas selecionadas.
            - Custo total.
        """
        result = []

        i = 0
        e = 0

        total_cost = 0

        self.graph = sorted(
            self.graph,
            key=lambda item: item[2],
            reverse=True
        )

        parent = []
        rank = []

        for node in range(self.v):
            parent.append(node)
            rank.append(0)

        while e < self.v - 1:

            u, v, w = self.graph[i]
            i += 1

            x = self.find_root(parent, u)
            y = self.find_root(parent, v)

            if x != y:

                e += 1

                result.append([u, v, w])

                total_cost += w

                self.union_sets(parent, rank, x, y)

        return result, total_cost


if __name__ == '__main__':

    g = Graph(8)

    g.add_edge(4, 7, 1)
    g.add_edge(5, 6, 2)
    g.add_edge(4, 5, 3)
    g.add_edge(6, 7, 4)
    g.add_edge(0, 1, 5)
    g.add_edge(3, 7, 6)
    g.add_edge(2, 5, 7)
    g.add_edge(2, 6, 8)
    g.add_edge(1, 2, 9)
    g.add_edge(1, 6, 10)
    g.add_edge(1, 5, 11)
    g.add_edge(1, 7, 13)
    g.add_edge(1, 4, 14)
    g.add_edge(0, 4, 15)
    g.add_edge(0, 3, 16)
    g.add_edge(3, 6, 17)
    g.add_edge(0, 7, 18)

    inicio = time.perf_counter()

    maximum_tree, total_cost = g.execute_maximum_kruskal()

    fim = time.perf_counter()

    tempo_execucao = (fim - inicio) * 1000

    print("=== ÁRVORE GERADORA MÁXIMA ===\n")

    print("Rotas selecionadas:\n")

    for u, v, peso in maximum_tree:

        print(
            f"Cidade {u} -> Cidade {v} | "
            f"Custo: {peso}"
        )

    print(f"\nCusto total da rede: {total_cost}")

    print(
        f"Tempo de execução: "
        f"{tempo_execucao:.4f} ms"
    )