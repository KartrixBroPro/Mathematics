from collections import deque
def bfs(graph,start):
    visited=set()
    queue=deque([start])
    order=[]

    visited.add(start)

    while queue:
        node=queue.popleft()
        order.append(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return order

def dfs(graph,start):
    visited=set()
    order=[]
    def dfs_recursive(node):
        visited.add(node)
        order.append(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                dfs_recursive(neighbour)
    dfs_recursive(start)
    return order

graph={
    'A':['B','C'],
    'B':['f','d'],
    'C':['s','j'],
    'f':[],
    'd':[],
    's':[],
    'j':[],
}
print("bfs",bfs(graph,'A'))
print("dfs",dfs(graph,'A'))
