
from itertools import permutations

def tsp_distance(route,distance_matrix):
    distance=0
    for i in range(len(route)-1):
        distance+=distance_matrix[route[i]][route[i+1]]
    distance+=distance_matrix[route[-1]][route[0]]
    return distance
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n=len(distance_matrix)
cities=list(range(n))
shortest_distance=float('inf')
best_route=None

for route in permutations(cities):
    distance=tsp_distance(route,distance_matrix)
    if shortest_distance>distance:
        shortest_distance=distance
        best_route=route
print(f"Shortest Distance ={shortest_distance}")
print(f"Route: {best_route}")
