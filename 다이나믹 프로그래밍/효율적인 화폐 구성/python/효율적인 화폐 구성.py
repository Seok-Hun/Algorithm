N, M = map(int,input().split())

C = []
for n in range(N):
    C.append(int(input()))

C.sort(reverse=True)

DP = 0
idx = 0
output = 0

while DP!=M:
    if idx==N:
        output = -1
        break
    if DP+C[idx]>M:
        idx+=1
    else:
        DP+=C[idx]
        output+=1

print(output)