#unweighted graphy 

graphy={}

n=int(input())

for i in range(n):
    u,v,weight=map(int,input().split())
    if u not in graphy:
        graphy[u]=[]
    graphy[u].append((v,weight))

print(graphy)

for source in graphy:
    print(f"source node is {source}")
    for neighbor,weight in graphy[source]:
        print(f"({neighbor}, weight={weight})",end=" ")
    print()
