N,M = map(int,input().split())
A,B,d = map(int,input().split())

ch = True

steps = [(0,-1),(1,0),(0,1),(-1,0)]

Map = []

for n in range(N):
    Map.append(list(map(int,input().split())))

Map[A][B] = 1

output = 1

def move(d):
    global A,B,Map,output
    if(B-1>=0 and d==3 and Map[A][B-1]!=1):
        B-=1
        output += 1
    elif(B+1<=M and d==1 and Map[A][B+1]!=1):
        B+=1
        output += 1
    elif(A-1>=0 and d==0 and Map[A-1][B]!=1):
        A-=1
        output += 1
    elif(A+1<=N and d==2 and Map[A+1][B]!=1):
        A+=1
        output += 1

while ch:
    d-=1
    if(d<0):d=3

    move(d)
    Map[A][B] = 1
    for step in steps:
        if Map[A+step[0]][B+step[1]]==0: 
            ch = True
            break
        ch = False

print(A," ",B)
print(output)