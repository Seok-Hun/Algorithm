N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

while min(A) < max(B) and K>0:
    A[A.index(min(A))], B[B.index(max(B))] = B[B.index(max(B))], A[A.index(min(A))]
    K-=1
    
print(sum(A))