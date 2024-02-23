N, M = map(int,input().split())
RCs = list(map(int,input().split()))

RCs.sort()

def search(array, target, start, end):
    mid = (start+end)//2
    sum = 0

    for el in array:
        if el-mid>0:
            sum+=el-mid

    if sum == target or start>=end:
        return mid
    elif sum > target:
        return search(array,target,mid+1,end)
    else:
        return search(array,target,start,mid-1)

print(search(RCs,M,0,max(RCs)))