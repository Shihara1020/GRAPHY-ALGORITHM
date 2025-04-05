import heapq

def spanningTree(graphy,n):
    connect=[False]*n
    heap=[(0,0)]  #weight,source
    sum=0

    while heap:
        weight,node=heapq.heappop(heap)
        if connect[node]:
            continue
        sum+=weight
        connect[node]=True

        for neibor,weight in graphy[node]:
            if not connect[neibor]:
                heapq.heappush(heap,(weight,neibor))