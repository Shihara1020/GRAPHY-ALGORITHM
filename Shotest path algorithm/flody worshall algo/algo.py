#All-Pairs Shortest Path
#Handles Negative Weights
#Detects Negative Cycles: If dist[i][i] < 0, a negative cycle exists.

def floyd_warshall(graph, n):
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0  # Distance from i to i is 0
    for u in range(n):
        for v, w in graph[u]:
            dist[u][v] = w  

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    for i in range(n):
        if dist[i][i] < 0:
            return "Negative cycle detected!"

    return dist