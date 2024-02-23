N = int(input())
products = list(map(int,input().split()))
products.sort()

M = int(input())
orders = list(map(int,input().split()))

output = []

def search(array,target,start,end):
    if start>end:
        return None
    
    mid = (start+end)//2

    if array[mid] == target:
        return array[mid]
    elif array[mid] > target:
        return search(array,target,start,mid-1)
    else :
        return search(array,target,mid+1,end)

for order in orders:
    result = search(products,order,0,N-1)
    if result == None:
        output.append("no")
    else :
        output.append("yes")

for i in range(len(output)):
    print(output[i],end=" ")