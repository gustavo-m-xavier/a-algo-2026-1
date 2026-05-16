"""
Problema:
Uma empresa deseja interligar 6 polos tecnológicos utilizando a menor
quantidade possível de cabos de rede/fibra óptica.

Os polos são:
A, B, C, D, E e F

As distâncias entre eles são representadas em quilômetros.

O algoritmo de Prim é utilizado para encontrar a
Árvore Geradora Mínima (MST), garantindo o menor custo total de conexão.
"""

import heapq


def prim(graph, start_node):
    """
    Executa o algoritmo de Prim para encontrar a
    Árvore Geradora Mínima (MST).

    Args:
        graph (dict): Grafo representado por lista de adjacência.
        start_node (str): Nó inicial.

    Returns:
        tuple:
            - mst_edges (list): Arestas da MST.
            - total_cost (int): Soma total dos pesos.
    """

    visited = set()
    min_heap = []
    mst_edges = []
    total_cost = 0

    visited.add(start_node)

    for neighbor, weight in graph[start_node]:
        heapq.heappush(min_heap, (weight, start_node, neighbor))

    while min_heap:
        weight, source, destination = heapq.heappop(min_heap)

        if destination in visited:
            continue

        visited.add(destination)

        mst_edges.append((source, destination, weight))
        total_cost += weight

        print(f"Conectando {source} --> {destination} ({weight} km)")

        for neighbor, new_weight in graph[destination]:
            if neighbor not in visited:
                heapq.heappush(
                    min_heap,
                    (new_weight, destination, neighbor)
                )

    return mst_edges, total_cost


graph = {
    "A": [("B", 4), ("C", 4)],
    "B": [("A", 4), ("C", 2), ("D", 5)],
    "C": [("A", 4), ("B", 2), ("D", 5), ("E", 6)],
    "D": [("B", 5), ("C", 5), ("E", 3), ("F", 4)],
    "E": [("C", 6), ("D", 3), ("F", 2)],
    "F": [("D", 4), ("E", 2)]
}

mst, cost = prim(graph, "A")

print("\nÁrvore Geradora Mínima:")
for source, destination, weight in mst:
    print(f"{source} --> {destination} = {weight} km")

print(f"\nCusto total da rede: {cost} km")