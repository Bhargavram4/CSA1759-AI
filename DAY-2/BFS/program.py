#BFS
from collections import deque
def bfs(graph,start_node):
    visited=set()
    queue=deque([start_node])
    travel=[]
    while queue:
        node=queue.popleft()
        if node not in visited:
            visited.add(node)
            travel.append(node)
        for neighbor in graph[node]:
            if neighbor  not  in visited:
                queue.append(neighbor)
    return travel




graph={
    'A':['E','B','G'],
    'B':['A','G','F','C','H'],
    'C':['B','H','D'],
    'D':['C','E'],
    'E':['A','D','F'],
    'F':['E','B'],
    'G':['A','B'],
    'H':['B','C'],
}
start_node='A'
order=bfs(graph,start_node)
print(f"BFS path is :{order}")
