#unweighted graphy 

#Number of the nodes
n=int(input())

graphy=[[0]*n for _ in range(n)]

#Number of edges
e =int(input())

for i in range(e):
    u,v=map(int,input().split())
    graphy[u][v]=1

print(graphy)

for row in graphy:
    print(" ".join(map(str,row)))