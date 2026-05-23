import random
import heapq


class Graph:
    """
    Classe responsável por representar um grafo não-direcionado
    utilizando lista de adjacência.
    """

    def __init__(self, num_nodes):
        """
        Inicializa o grafo com a quantidade de nós informada.

        :param num_nodes: Quantidade total de nós do grafo.
        """
        self.num_nodes = num_nodes
        self.graph = {i: [] for i in range(num_nodes)}

    def add_edge(self, source, destination, weight):
        """
        Adiciona uma aresta entre dois nós.

        :param source: Nó de origem.
        :param destination: Nó de destino.
        :param weight: Peso da aresta.
        """
        self.graph[source].append((destination, weight))
        self.graph[destination].append((source, weight))

    def generate_random_edges(self, connections_per_node=3, max_weight=20):
        """
        Gera conexões aleatórias entre os nós do grafo.

        :param connections_per_node: Quantidade de conexões por nó.
        :param max_weight: Peso máximo permitido para as arestas.
        """
        for node in range(self.num_nodes):
            for _ in range(connections_per_node):

                destination = random.randint(0, self.num_nodes - 1)

                while destination == node:
                    destination = random.randint(0, self.num_nodes - 1)

                weight = random.randint(1, max_weight)

                self.add_edge(node, destination, weight)

    def dijkstra(self, start_node, end_node):
        """
        Executa o algoritmo de Dijkstra para encontrar
        o menor caminho entre dois nós.

        :param start_node: Nó inicial.
        :param end_node: Nó final.

        :return:
            - Lista contendo o menor caminho.
            - Custo total do caminho.
        """

        distances = {
            node: float('inf')
            for node in self.graph
        }

        previous_nodes = {
            node: None
            for node in self.graph
        }

        distances[start_node] = 0

        priority_queue = [(0, start_node)]

        while priority_queue:

            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node]:

                new_distance = current_distance + weight

                if new_distance < distances[neighbor]:

                    distances[neighbor] = new_distance
                    previous_nodes[neighbor] = current_node

                    heapq.heappush(
                        priority_queue,
                        (new_distance, neighbor)
                    )

        path = []

        current = end_node

        while current is not None:
            path.append(current)
            current = previous_nodes[current]

        path.reverse()

        return path, distances[end_node]


def main():
    """
    Função principal responsável por:
    - Gerar o grafo aleatoriamente.
    - Escolher nós de início e fim.
    - Executar o algoritmo de Dijkstra.
    - Exibir o resultado no terminal.
    """

    num_nodes = random.randint(50, 150)

    graph = Graph(num_nodes)

    graph.generate_random_edges(
        connections_per_node=4,
        max_weight=30
    )

    start_node = random.randint(0, num_nodes - 1)
    end_node = random.randint(0, num_nodes - 1)

    while end_node == start_node:
        end_node = random.randint(0, num_nodes - 1)

    path, total_cost = graph.dijkstra(
        start_node,
        end_node
    )

    print("=" * 50)
    print(f"Número de nós: {num_nodes}")
    print(f"Primeiro nó: {start_node}")
    print(f"Último nó: {end_node}")
    print("=" * 50)

    if total_cost == float('inf'):
        print("Caminho não encontrado entre os nós")
    else:
        print("Menor caminho encontrado:")
        print(" -> ".join(map(str, path)))

        print(f"\n Custo Total: {total_cost}")


if __name__ == "__main__":
    main()