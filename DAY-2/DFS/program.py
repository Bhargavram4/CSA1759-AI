
def dfs(graph,node,visited=None):
    if visited is None:
        visited=set()
    visited.add(node)
    travel=[node]
    for neighbor in graph[node]:
        if neighbor not in visited:
            travel.extend(dfs(graph,neighbor,visited))
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
order=dfs(graph,start_node)
print(f"DFS path is :{order}")
