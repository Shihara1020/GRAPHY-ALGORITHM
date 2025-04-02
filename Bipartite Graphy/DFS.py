def is_bipartite(graph):
    n = len(graph)
    colors = [""] * n  # "RED", "GREEN", or "" (unvisited)
    
    def dfs(node, color):
        colors[node] = color
        for neighbor in graph[node]:
            if not colors[neighbor]:
                new_color = "GREEN" if color == "RED" else "RED"
                if not dfs(neighbor, new_color):
                    return False
            elif colors[neighbor] == color:
                return False  # Same color → not bipartite
        return True  # All neighbors processed successfully
    
    for node in range(n):
        if not colors[node]:  # Start DFS for unvisited nodes
            if not dfs(node, "RED"):
                return False
    return True