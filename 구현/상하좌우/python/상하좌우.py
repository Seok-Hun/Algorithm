N = input()
List = list(map(str,input().split()))

X,Y = 1,1

for way in List:
    match way:
        case 'R':
            if(X==N):continue
            X+=1
        case 'L':
            if(X==1):continue
            X-=1
        case 'U':
            if(Y==1):continue
            Y-=1
        case 'D':
            if(Y==N):continue
            Y+=1

print(X," ",Y)