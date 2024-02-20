N,K = map(int, input().split())
output = 0

while(N!=1):
    if(N%K==0):
        N/=K
    else:
        N-=1
    output += 1

print(output)