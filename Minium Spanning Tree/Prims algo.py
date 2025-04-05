import heapq

def prim_mst(graph, n):
    connected = [False] * n  # Tracks connected nodes
    heap = [(0, 0)]  # (weight, node)
    mst_weight = 0  # Total weight of MST
    edges_used = 0  # Track edges added (optimization)

    while heap and edges_used < n - 1:
        weight, node = heapq.heappop(heap)
        if connected[node]:
            continue  # Skip if already connected
        connected[node] = True
        mst_weight += weight
        edges_used += 1

        for neighbor, edge_weight in graph[node]:
            if not connected[neighbor]:
                heapq.heappush(heap, (edge_weight, neighbor))

    return mst_weight if edges_used == n - 1 else -1  # -1 if graph is disconnected