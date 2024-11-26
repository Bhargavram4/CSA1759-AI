
def vaccum_cleaner(environment,start):
    row=len(environment)
    col=len(environment[0])
    x,y=start
    action=[]
    while True:
        if environment[x][y]==1:
            environment[x][y]=0
            action.append(f"Room Cleand at ({x},{y})")
        if all(room==0 for row in environment for room in row):
            action.append("All rooms are Cleaned.Stopping.................")
            break
        if y+1<col:
            y+=1
        elif x+1<row:
            x+=1
            y=0
        else:
            break
        action.append(f"Move to Room at ({x},{y})")
    return action,environment

environment=[[1,0,1],[1,1,1],[0,0,1]]
start=(0,0)
actions,cleaned=vaccum_cleaner(environment,start)

print("Actions done by vaccum cleaner:")
for action in actions:
    print(action)
print("Cleaned Environment is: ")
for row in cleaned:
    print(row)
