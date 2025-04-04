from collections import deque
result=[]

def DFS(vertex,graphy):
    visited=set()
    stack=[vertex]
    visited.add(vertex)

    while stack:
        out=stack.pop()
        result.append(out)
        for member in reversed(graphy[out]):
            if member not in visited:
                visited.append(member)
                stack.append(member)
    return result


