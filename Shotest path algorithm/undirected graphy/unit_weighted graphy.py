from collections import deque

def shortest_path_unweighted(graph, n, source):
    distance = [float('inf')] * n
    distance[source] = 0  # Distance to source is 0
    visited = [False] * n
    q = deque([source])
    visited[source] = True

    while q:
        u = q.popleft()
        for v in graph[u]:  # For each neighbor
            if not visited[v]:
                distance[v] = distance[u] + 1  # Update distance
                visited[v] = True  # Mark as visited
                q.append(v)  # Enqueue for further processing
    return distance