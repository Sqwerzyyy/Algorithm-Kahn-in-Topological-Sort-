def run_experiments():
    #параметри експерименту
    #розміри графів (кількість вершин)
    sizes = [10, 50, 100, 200, 300, 400, 500]
    #щільність(0.1 = розріджений, 0.5 = середній, 0.8 = щільний)
    densities = [0.1, 0.5, 0.8]

    results = {
        'list': {d: {'sizes': [], 'times': []} for d in densities},
        'matrix': {d: {'sizes': [], 'times': []} for d in densities}
    }

    print(f"{'Type':<10} | {'Density':<10} | {'Size':<10} | {'Time (s)':<15}")
    print("-" * 50)

    for rep_type in ['list', 'matrix']:
        for density in densities:
            for n in sizes:
                # генеруємо граф
                g = Graph.generate_random_dag(n, density, rep_type)

                # заміряємо час
                start_time = time.perf_counter()
                g.sort()
                end_time = time.perf_counter()

                execution_time = end_time - start_time

                #зберігаємо результати
                results[rep_type][density]['sizes'].append(n)
                results[rep_type][density]['times'].append(execution_time)

                print(f"{rep_type:<10} | {density:<10} | {n:<10} | {execution_time:.6f}")

    return results, sizes, densities