from collections import deque

def is_cyclic_bfs(graph, n):
    visited = [0] * n
    
    for node in range(n):
        if not visited[node]:
            q = deque([(node, -1)])  # (current_node, parent_node)
            visited[node] = 1
            
            while q:
                current, parent = q.popleft()
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = 1
                        q.append((neighbor, current))
                    elif neighbor != parent:  # Cycle detected!
                        return True
    return False