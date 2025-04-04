def topological_sort(graph, n):
    visited = [False] * n
    topo_order = []
    
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        topo_order.append(node)  
    
    for node in range(n):
        if not visited[node]:
            dfs(node)
    
    return topo_order[::-1] 