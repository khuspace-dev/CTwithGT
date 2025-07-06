N = input()
plan = list(map(str, input().split()))

curPoint = [ 1, 1 ]

for direction in plan:
    if(direction == "U"):
        if(curPoint[0] == 1):
            continue
        curPoint[0] -= 1
    elif(direction == "D"):
        if(curPoint[0] == N):
            continue
        curPoint[0] += 1
    elif(direction == "L"):
        if(curPoint[1] == 1):
            continue
        curPoint[1] -= 1
    elif(direction == "R"):
        if(curPoint[1] == N):
            continue
        curPoint[1] += 1
        
print(curPoint)