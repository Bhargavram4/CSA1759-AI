
from collections import deque
def safe(state):
    ML,CL,MR,CR,_=state
    if  (ML<CL and ML>0) or (MR<CR and MR>0):
        return False
    if ML<0 or CL<0 or MR<0 or CR<0:
        return False
    return True
def nStates(state):
    newStates=[]
    ML,CL,MR,CR,boat=state
    moves=[(1,0),(2,0),(0,1),(0,2),(1,1)]
    for M,C in moves:
        if boat=='left':
            newState=(ML-M,CL-C,MR+M,CR+C,'right')
        else:
            newState=(ML+M,CL+C,MR-M,CR-C,'left')
        if safe(newState):
            newStates.append(newState)
    return newStates
def missionaries_and_cannibals():
    initial=(3,3,0,0,'left')
    goal=(0,0,3,3,'right')
    queue=deque([(initial,[])])
    while queue:
        state,path=queue.popleft()
        visited=set()
        if state in visited:
            continue
        visited.add(state)

        if state==goal:
            return path+[state]

        for nState in nStates(state):
            queue.append((nState,path+[state]))
    return None
ans=missionaries_and_cannibals()
if ans:
    print('Solution is : ')
    for step in ans:
        print(step)
else:
    print("Solution Not Found")
