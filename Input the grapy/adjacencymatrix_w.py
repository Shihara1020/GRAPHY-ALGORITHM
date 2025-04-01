#unweighted graphy 

#Number of the nodes
n=int(input())

graphy=[[0]*n for _ in range(n)]

#Number of edges
e =int(input())

for i in range(e):
    u,v,weight=map(int,input().split())
    graphy[u][v]=weight

print(graphy)

for row in graphy:
    print(" ".join(map(str,row)))