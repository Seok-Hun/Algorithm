N = int(input())
K = list(map(int,input().split()))

DP = [0]*100

DP[0] = K[0]
DP[1] = max(K[0],K[1])
for n in range(2,N):
    DP[n] = max(DP[n-1],DP[n-2]+K[n])
print(DP[N-1])