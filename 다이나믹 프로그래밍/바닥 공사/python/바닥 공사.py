N = int(input())

DP = [0]*1000

DP[0] = 1
DP[1] = 3

for n in range(2,N):
    DP[n] = DP[n-1]+2*DP[n-2]

print(DP[N-1]%796796)