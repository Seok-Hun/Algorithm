from collections import deque

queue = deque()

N, M = map(int, input().split())

maze = []
for n in range(N):
    maze.append(list(map(int,input())))

def BSF(Y,X):
    global maze
    queue.append((Y,X))
    while queue:
        v = queue.popleft()
        y,x = v[0],v[1]
        if y==N-1 and x==M-1:
            break
        next = maze[y][x]+1
        if x-1>0 and maze[y][x-1]==1:
            queue.append((y,x-1))
            maze[y][x-1]=next
        if x+1<M and maze[y][x+1]==1:
            queue.append((y,x+1))
            maze[y][x+1]=next
        if y-1>0 and maze[y-1][x]==1:
            queue.append((y-1,x))
            maze[y-1][x]=next
        if y+1<N and maze[y+1][x]==1:
            queue.append((y+1,x))
            maze[y+1][x]=next

BSF(0,0)
print(maze[N-1][M-1])