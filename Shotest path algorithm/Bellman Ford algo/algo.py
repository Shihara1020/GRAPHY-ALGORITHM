#find the shortest path from a source node to all other nodes 
#Handles Negative weights
#detects negative cycles


def bellman_ford(graph, n, source):
    dist = [float('inf')] * n
    dist[source] = 0

    for _ in range(n - 1):
        for u in range(n):
            for v, w in graph[u]:
                if dist[u] != float('inf') and dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w

    for u in range(n):
        for v, w in graph[u]:
            if dist[u] != float('inf') and dist[v] > dist[u] + w:
                return "Negative cycle detected!"

    return dist