def has_cycle_dfs(graph):
    visited = [False] * len(graph)
    
    def dfs(node, parent):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):  # Recursive call
                    return True
            elif neighbor != parent:     # Cycle detected!
                return True
        return False
    
    for node in range(len(graph)):
        if not visited[node]:
            if dfs(node, -1):  # Start DFS with parent=-1 (no parent)
                return True
    return False