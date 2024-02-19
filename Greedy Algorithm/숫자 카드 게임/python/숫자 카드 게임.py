N, M = map(int, input().split())
output = 0

for i in range(M):
    data = list(map(int, input().split()))
    if(min(data)>output):
        output = min(data)

print(output)