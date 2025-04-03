from collections import defaultdict, deque

def shortest_path_dag(graph, n, source):
    # Step 1: Topological Sort (Kahn's Algorithm)
    in_degree = [0] * n
    for u in range(n):
        for v, _ in graph[u]:
            in_degree[v] += 1

    queue = deque([u for u in range(n) if in_degree[u] == 0])
    topo_order = []

    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v, _ in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    # Step 2: Initialize distances
    dist = [float('inf')] * n
    dist[source] = 0  # Distance to source is 0

    # Step 3: Relax edges in topological order
    for u in topo_order:
        if dist[u] != float('inf'):  # Only process reachable nodes
            for v, weight in graph[u]:
                if dist[v] > dist[u] + weight:  # Relaxation
                    dist[v] = dist[u] + weight

    return dist