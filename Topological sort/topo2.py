def topological_sort(graph, n):
    visited = [False] * n
    path = [False] * n  # Track nodes in current DFS path
    topo_order = []
    
    def dfs(node):
        visited[node] = True
        path[node] = True  # Mark as in current path
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor):  # If cycle found downstream
                    return True
            elif path[neighbor]:  # Corrected: Check if neighbor is in current path
                return True  # Cycle detected
        
        topo_order.append(node)
        path[node] = False  # Backtrack: remove from current path
        return False
    
    for node in range(n):  # Important: iterate through all nodes (0 to n-1)
        if not visited[node]:
            if dfs(node):
                return []  # Cycle exists
    
    return topo_order[::-1]  # Reverse post-order to get topological sort