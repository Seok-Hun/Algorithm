N, M, K = map(int, input().split())
List = list(map(int, input().split()))
List.sort(reverse=True)
output = 0

# 반복문 사용
# for i in range(M):
#     if(i%K==1 and i>K):
#         output += List[1]
#         continue
#     output += List[0]

# 반복문 미사용
count = M//(K+1)

firstSet = List[0]*(M-count)
seconfSet = List[1]*count

print(firstSet+seconfSet)