import time
import random
from collections import deque
#1 Kahn's Algorithms (2 Implementations)
def kahn_sort_adjacency_list(n_vertices, graph, in_degree):
    """
    Implementation for Adjacency List.
    """
    # ініціалізація черги вершинами з нульовим вхідним степенем
    queue = deque([v for v in range(n_vertices) if in_degree[v] == 0])
    topo_order = []
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        # проходимось тільки по існуючих сусідах (ефективно для розріджених графів)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    return topo_order

def kahn_sort_adjacency_matrix(n_vertices, graph, in_degree):
    """
    implementation for adjacency matrix.
    """
    queue = deque([v for v in range(n_vertices) if in_degree[v] == 0])
    topo_order = []
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        # мусимо перевірити весь рядок матриці, щоб знайти сусідів (повільно для великих графів)
        for v in range(n_vertices):
            if graph[u][v] == 1:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
    return topo_order
# random DAG gener
def generate_random_dag(n, density, rep_type):
    """
    generates a random DAG to avoid cycles
    """
    in_degree = {i: 0 for i in range(n)}
    edge_count = 0
    if rep_type == 'list':
        graph = {i: [] for i in range(n)}
        # проходимо по верхньому трикутнику матриці (i < j), щоб не було циклів
        for i in range(n):
            for j in range(i + 1, n):
                if random.random() < density:
                    graph[i].append(j)
                    in_degree[j] += 1
                    edge_count += 1
    elif rep_type == 'matrix':
        graph = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if random.random() < density:
                    graph[i][j] = 1
                    in_degree[j] += 1
                    edge_count += 1
    return graph, in_degree, edge_count
#3 experiments and benchmark
def run_experiments():
    #параметри експериментів
    sizes = [100, 300, 500]  # кількість вершин
    densities = [0.1, 0.5, 0.8]  # щільність (10%, 50%, 80%)
    repeats = 5  # кількість повторів для усереднення результату
    # заголовок таблиці
    print(f"\n{'Rep Type':<10} | {'Nodes':<6} | {'Density':<8} | {'Avg Time (s)':<12} | {'Edges (Actual)'}")
    print("-" * 65)
    # 1 тестування списку суміжності (adjacency list)
    for n in sizes:
        for d in densities:
            total_time = 0
            avg_edges = 0

            for _ in range(repeats):
                #етап генерації (не враховую в час виконання алгоритму)
                graph, in_degree, edges = generate_random_dag(n, d, 'list')
                in_degree_copy = in_degree.copy()

                # етап замірів часу (тільки чистий алгоритм)
                start = time.perf_counter()
                kahn_sort_adjacency_list(n, graph, in_degree_copy)
                end = time.perf_counter()

                total_time += (end - start)
                avg_edges = edges

            avg_time = total_time / repeats
            print(f"{'List':<10} | {n:<6} | {d:<8} | {avg_time:.6f}     | {avg_edges}")

    print("-" * 65)

    # 2 тестування матриці суміжності (adjacency matrix)
    for n in sizes:
        for d in densities:
            total_time = 0
            avg_edges = 0
            for _ in range(repeats):
                #генерація матриці
                graph, in_degree, edges = generate_random_dag(n, d, 'matrix')
                in_degree_copy = in_degree.copy()

                # заміри часу
                start = time.perf_counter()
                kahn_sort_adjacency_matrix(n, graph, in_degree_copy)
                end = time.perf_counter()

                total_time += (end - start)
                avg_edges = edges

            avg_time = total_time / repeats
            print(f"{'Matrix':<10} | {n:<6} | {d:<8} | {avg_time:.6f}     | {avg_edges}")

if __name__ == "__main__":
    run_experiments()