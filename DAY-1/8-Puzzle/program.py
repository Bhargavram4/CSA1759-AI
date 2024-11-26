

from collections import deque as puzzle
def is_solvable(start_state):
    inv=0
    for i in range(len(start_state)):
        for j in range(i+1,len(start_state)):
            if start_state[i]>start_state[j]!=0:
                inv+=1
    return inv%2==0

def get_neighbours(state):
    neighbours=[]
    zero_index=state.index(0)
    x,y=divmod(zero_index,3)
    moves=[(-1,0),(1,0),(0,-1),(0,1)]
    for dx,dy in moves:
        new_x,new_y=x+dx,y+dy
        if 0<=new_x<3 and 0<=new_y<3:
            new_index=new_x*3+new_y
            new_state=state[:]
            new_state[zero_index],new_state[new_index]=new_state[new_index],new_state[zero_index]
            neighbours.append(new_state)
    return neighbours
def bfs(start_state,goal_state):
    queue=puzzle([(start_state,[])])
    visited=set()
    while queue:
        state,path=queue.popleft()
        if state==goal_state:
            return path+[state]
        visited.add(tuple(state))
        for neighbours in get_neighbours(state):
            if tuple(neighbours) not in visited:
                queue.append((neighbours,path+[state]))
    return None


start_state=[1,2,3,4,0,5,6,7,8]
goal_state=[1,2,3,4,5,6,7,8,0]
if is_solvable:
    solution=bfs(start_state,goal_state)
    if solution:
        print("Steps:   ")
        for step in solution:
            for i in range(0,9,3):
                print(step[i:i+3])
            print()
    else:
        print("No Solution..")
else:
    print("Not solvable")
