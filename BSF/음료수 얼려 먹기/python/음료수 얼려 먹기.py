from collections import deque

queue = deque()

N,M = map(int,input().split())

output = 0

ice = []
for n in range(N):
    ice.append(list(map(int,input())))

def BSF(Y, X):
    global ice
    queue.append((Y,X))
    ice[Y][X] = 1
    while queue:
        v = queue.popleft()
        x,y = v[1],v[0]
        if x+1<M and ice[y][x+1] == 0:
            queue.append((y,x+1))
            ice[y][x+1] = 1
        if x-1>0 and ice[y][x-1] ==0:
            queue.append((y,x-1))
            ice[y][x-1] = 1
        if y+1<N and ice[y+1][x] == 0:
            queue.append((y+1,x))
            ice[y+1][x] = 1
        if y-1>0 and ice[y-1][x] == 0:
            queue.append((y-1,x))
            ice[y-1][x] = 1

for y in range(N):
    for x in range(M):
        if ice[y][x] == 0:
            BSF(y,x)
            output += 1

print(output)
