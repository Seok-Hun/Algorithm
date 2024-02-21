N = int(input())

nums = []
for n in range(N):
    nums.append(int(input()))

nums.sort(reverse=True)

for n in nums:
    print(n,end=' ')