from collections import deque

def is_bipartite(graph):
    if not graph:
        return True
    
    n = len(graph)
    color = [""] * n  # Track colors ("RED", "GREEN", or "")
    for src in range(n):
        if not color[src]:  # Start BFS if unvisited
            queue = deque([(src, "RED")])
            color[src] = "RED"
            
            while queue:
                node, current_color = queue.popleft()
                for neighbor in graph[node]:
                    if not color[neighbor]:
                        # Assign opposite color
                        new_color = "GREEN" if current_color == "RED" else "RED"
                        color[neighbor] = new_color
                        queue.append((neighbor, new_color))
                    elif color[neighbor] == current_color:
                        return False  # Same color → not bipartite
    return True