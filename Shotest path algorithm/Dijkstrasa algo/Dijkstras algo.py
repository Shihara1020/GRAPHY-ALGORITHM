import heapq

def dijkstra(graph, n, source):
    distance = [float('inf')] * n
    distance[source] = 0
    heap = [(0, source)]  # (current_distance, node)
    visited = set()  # Track visited nodes to avoid reprocessing

    while heap:
        current_dist, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)

        for v, weight in graph[u]:
            if distance[v] > current_dist + weight:
                distance[v] = current_dist + weight
                heapq.heappush(heap, (distance[v], v))
    
    return distance