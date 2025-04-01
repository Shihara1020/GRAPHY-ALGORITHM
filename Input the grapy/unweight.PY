#unweighted graphy 

graphy={}

n=int(input())

for i in range(n):
    u,v=map(int,input().split())
    if u not in graphy:
        graphy[u]=[]
    graphy[u].append(v)

print(graphy)

for source in graphy:
    print("source node is "+str(source))
    for neighbor in graphy[source]:
        print(neighbor,end=" ")
    print()
