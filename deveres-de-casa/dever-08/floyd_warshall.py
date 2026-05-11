"""
PROBLEMA DO DIA A DIA
=====================

Uma empresa de entregas possui vários centros de distribuição conectados
por estradas. Cada estrada possui um custo de deslocamento entre dois pontos.

O objetivo é descobrir o menor custo possível entre TODOS os centros,
mesmo que seja necessário passar por centros intermediários.

O algoritmo de Floyd-Warshall é ideal para esse cenário, pois calcula
o menor caminho entre todos os pares de vértices de um grafo.

Neste exemplo:
- Cada centro de distribuição é um vértice.
- Cada estrada é uma aresta com custo.
- O algoritmo encontra as rotas mais baratas possíveis.
"""


class FloydWarshall:
    """
    Implementação do algoritmo de Floyd-Warshall.

    O algoritmo calcula o menor caminho entre todos
    os pares de vértices de um grafo ponderado.
    """

    def __init__(self, vertices):
        """
        Inicializa a matriz de distâncias.

        :param vertices: Lista com os nomes dos vértices.
        """
        self.vertices = vertices
        self.size = len(vertices)

        self.distances = [
            [float("inf")] * self.size
            for _ in range(self.size)
        ]

        for index in range(self.size):
            self.distances[index][index] = 0

    def add_edge(self, source, destination, cost):
        """
        Adiciona uma conexão entre dois vértices.

        :param source: Vértice de origem.
        :param destination: Vértice de destino.
        :param cost: Custo da conexão.
        """
        source_index = self.vertices.index(source)
        destination_index = self.vertices.index(destination)

        self.distances[source_index][destination_index] = cost

    def run(self):
        """
        Executa o algoritmo de Floyd-Warshall.

        O algoritmo testa todos os vértices como
        possíveis intermediários para melhorar
        os caminhos existentes.
        """
        print("\n========== EXECUTANDO FLOYD-WARSHALL ==========\n")

        for intermediate in range(self.size):

            print(
                f"Usando '{self.vertices[intermediate]}' "
                f"como vértice intermediário...\n"
            )

            for source in range(self.size):
                for destination in range(self.size):

                    current_distance = self.distances[source][destination]

                    new_distance = (
                        self.distances[source][intermediate]
                        + self.distances[intermediate][destination]
                    )

                    if new_distance < current_distance:

                        print(
                            f"Melhor caminho encontrado:\n"
                            f"{self.vertices[source]} -> "
                            f"{self.vertices[destination]}\n"
                            f"Custo antigo: {current_distance}\n"
                            f"Novo custo : {new_distance}\n"
                        )

                        self.distances[source][destination] = new_distance

            self.print_matrix()

    def print_matrix(self):
        """
        Exibe a matriz de menores distâncias.
        """
        print("Matriz atual de menores caminhos:\n")

        header = "\t".join(self.vertices)
        print(f"\t{header}")

        for row_index in range(self.size):

            row_values = []

            for column_index in range(self.size):

                value = self.distances[row_index][column_index]

                if value == float("inf"):
                    row_values.append("INF")
                else:
                    row_values.append(str(value))

            row_text = "\t".join(row_values)

            print(f"{self.vertices[row_index]}\t{row_text}")

        print("\n" + "=" * 50 + "\n")


# =====================================
# EXEMPLO PRÁTICO
# =====================================

distribution_centers = [
    "Centro A",
    "Centro B",
    "Centro C",
    "Centro D"
]

graph = FloydWarshall(distribution_centers)

# Estradas entre centros
graph.add_edge("Centro A", "Centro B", 4)
graph.add_edge("Centro A", "Centro C", 11)

graph.add_edge("Centro B", "Centro C", 2)
graph.add_edge("Centro B", "Centro D", 5)

graph.add_edge("Centro C", "Centro D", 1)

graph.add_edge("Centro D", "Centro A", 3)

print("Matriz inicial:\n")
graph.print_matrix()

graph.run()

print("========== RESULTADO FINAL ==========\n")
graph.print_matrix()