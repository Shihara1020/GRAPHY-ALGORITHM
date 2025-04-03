from collections import deque

def topological_sort_kahn(graph, n):
    in_degree = [0] * n
    for u in range(n):
        for v in graph[u]:
            in_degree[v] += 1

    queue = deque([u for u in range(n) if in_degree[u] == 0])
    topo_order = []

    while queue:
        u = queue.popleft()
        topo_order.append(u)

        for v in graph[u]:  # Remove edges u → v
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(topo_order) == n:
        return topo_order  # Valid topological order
    else:
        return []  # Cycle detected (not a DAG)