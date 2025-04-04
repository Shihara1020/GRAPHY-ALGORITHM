n=int(input)
visited=[False]*n
results=[]
def dfs(node,graphy):
    visited[node]=True
    results.append(node)
    for neighbor in graphy[node]:
        if not visited[neighbor]:
            dfs(neighbor)
            