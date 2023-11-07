def quick_sort(arr,n):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2][n]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num[n] < pivot:
            lesser_arr.append(num)
        elif num[n] > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr,n) + equal_arr + quick_sort(greater_arr,n)

def find(parents, x):
    if parents[x] != x:
        find(parents,parents[x])
    return parents[x]

def union(parents, a, b):
    a = find(parents,a)
    b = find(parents,b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


def kruskal(stations, edges):
    sorted_edges = quick_sort(edges,0)
    result_list = []
    for i in range(0,len(stations)):
        a = sorted_edges[i][1]
        b = sorted_edges[i][2]
        if find(parents,a) != find(parents,b):
            union(parents, a, b)
            result_list.append(sorted_edges[i])
    return result_list

stations = ['A','B','C','D','E','F','G']
edges=[
(7, 'A', 'B'),
(15, 'A', 'C'),
(8, 'B', 'C'),
(9, 'B', 'D'),
(8, 'C', 'D'),
(11, 'D', 'E'),
(6, 'D', 'F'),
(8, 'E', 'F'),
(4, 'E', 'G'),
(7, 'F', 'G')
]

parents={}
for i in stations:
    parents[i]=i

print(kruskal(stations, edges))

