from collections import deque

def bfs(start, graph):
    visited = [False] * (len(graph) + 1)  # For 1-based indexing
    q = deque([start])
    visited[start] = True
    result = []
    
    while q:
        u = q.popleft()
        result.append(u)
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    
    return result