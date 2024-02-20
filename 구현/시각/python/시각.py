N = int(input())

M = 59
S = 59

output=0

for n in range(N+1):
    for m in range(M+1):
        for s in range(S+1):
            if '3' in str(n)+str(m)+str(s):
                output+=1

print(output)