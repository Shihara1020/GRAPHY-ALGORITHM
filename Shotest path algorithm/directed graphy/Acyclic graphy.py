from collections import deque

def shortest_path_dag(graph, n, source):
    in_degree = [0] * n
    for u in range(n):
        for v, weight in graph[u]:
            in_degree[v] += 1  # Count incoming edges

    distance = [float('inf')] * n
    distance[source] = 0  # Distance to source is 0
    q = deque([u for u in range(n) if in_degree[u] == 0])

    while q:
        u = q.popleft()
        
        for v, weight in graph[u]:
            # Relaxation step
            if distance[v] > distance[u] + weight:
                distance[v] = distance[u] + weight
            
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)

    return distance