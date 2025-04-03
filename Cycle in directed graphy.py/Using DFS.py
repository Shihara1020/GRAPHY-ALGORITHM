def has_cycle_directed(graph):
    n = len(graph)
    visited = [False] * n  # Track fully processed nodes
    recursion_stack = [False] * n  # Track nodes in current DFS path
    
    def dfs(node):
        recursion_stack[node] = True
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor):  # Recursively check neighbors
                    return True
            elif recursion_stack[neighbor]:  # Back edge detected (cycle)
                return True
        
        # Backtrack: remove node from recursion stack
        recursion_stack[node] = False
        return False
    
    # Check all nodes in case of disconnected components
    for node in range(n):
        if not visited[node]:
            if dfs(node):
                return True
    return False