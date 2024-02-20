V = input()

X = int(V[1])
Y = ord(V[0])

output=0

def check(X,Y):
    if(X>8 or X<1 or Y<ord('a') or Y>ord('h')):
        return False
    return True

if check(X-2,Y-1): output+=1
if check(X-1,Y-2): output+=1
if check(X+1,Y-2): output+=1
if check(X+2,Y-1): output+=1
if check(X-1,Y+2): output+=1
if check(X-2,Y+1): output+=1
if check(X+1,Y+2): output+=1
if check(X+2,Y+1): output+=1

print(output)