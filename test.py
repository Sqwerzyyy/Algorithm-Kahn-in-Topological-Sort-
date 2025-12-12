# 1 спершу готуємо дані  - НЕ ВРАХОВУЄМО!!!!!!
graph, in_degree, edges = generate_random_dag(n, d, 'list')
in_degree_copy = in_degree.copy()
# 2 вмикаємо секундомір
start = time.perf_counter()
# 3 виконуємо онлі алгоритм - ВРАХОВУЄМО!!!!!
kahn_sort_adjacency_list(n, graph, in_degree_copy)
# 4 вимикаємо секундомір
end = time.perf_counter()
# 5 записуємо чистий фіанальний час
total_time += (end - start)