import heapq

def dijkstra(graph, source, n, dest):
    dis = [float('inf')] * n
    dis[source] = 0
    heap = [(0, source)]
    parent = [-1] * n  # Initialize all parents to -1 (no parent)

    while heap:
        weight, node = heapq.heappop(heap)
        if node == dest:
            break  # Early exit if destination is reached
        if weight > dis[node]:
            continue  # Skip if a better path already exists
        for neighbor, w in graph[node]:
            if dis[neighbor] > weight + w:
                dis[neighbor] = weight + w
                parent[neighbor] = node  # Update parent
                heapq.heappush(heap, (dis[neighbor], neighbor))

    if dis[dest] == float('inf'):
        return "No path"  # No path exists

    # Reconstruct the path from destination to source
    path = []
    node = dest
    while node != -1:  # Backtrack until source (parent[source] = -1)
        path.append(node)
        node = parent[node]
    
    return path[::-1]  # Reverse to get source → destination