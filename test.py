import heapq


def dijkstra(grapy,source,n,dest):
    dis=[float("inf")]*n
    dis[source]=0
    heap=[(0,source)]
    parent=[-1]*n
    while heap:
        weight,node=heapq.heappop(heap)
        if node==dest:
            break
        for neibor,w in grapy[node]:
            if dis[neibor]>w+weight:
                dis[neibor]=w+weight
                heapq.heappush(heap,(dis[neibor],neibor))
                parent[neibor]=node
    if dis[dest]==float("inf"):
        return "No path"
    path=[]
    node=dest
    while parent[node]!=node:
        path.append(node)
        node=parent[node]

    path.append(source)
            