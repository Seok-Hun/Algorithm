# 퀵 정렬 함수
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

# x에 해당하는 정점과 연결된 최상위 정점을 구하는 함수
def find(parents, x):
# x 정점과 x 정점의 최상위 정점이 같다면 x 정점이 최상위 정점이라는 것을 의미
# 만약 x와 x에 해당하는 정점의 최상위 정점의 값이 다르다면 x 정점이 다른 정점과 연결되었다는 의미
# x 정점에 연결된 다른 정점을 거슬러 올라간다.
# 재귀 연산으로 이를 반복하여 최상위에 위치한 정점을 찾는다.
    if parents[x] != x:
        find(parents,parents[x])
# x 정점의 최상위 정점값을 반환한다.
    return parents[x]

# 두개의 정점의 최상위 정점을 통일하여 정점들을 연결하는 함수
# a, b : 각각 하나의 간선에 연결된 두 정점들을 의미한다.
def union(parents, a, b):
# 각각의 정점들의 최상위 정점을 구한다.
    a = find(parents,a)
    b = find(parents,b)
# 가장 낮은 값의 정점을 최상위 정점으로 삼는다.
# 높은 값의 최상위 정점의 value에 낮은 값의 정점을 넣어 두 정점들을 연결한다.
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

# 크루스칼 알고리즘 구현
def kruskal(stations, edges):
# 간선 리스트를 간선 가중치 오름차순으로 정렬
    sorted_edges = quick_sort(edges,0)
# 결과값을 저장할 리스트 선언
    result_list = []
# 정점들의 개수만큼 반복문 작동
    for i in range(0,len(stations)):
# a, b : 하나의 간선과 연결된 각각의 정점들
        a = sorted_edges[i][1]
        b = sorted_edges[i][2]
# 두 정점들의 최상위 정점이 다르다면 두 정점들이 서로 연결되어있지 않다는 의미
# 최상위 정점이 같아 연결된 것을 확인하면 사이클을 형성하는 간선은 해당 조건문을 건너뛰어 경로 추가되지 않는다.
        if find(parents,a) != find(parents,b):
# 두 정점들을 서로 연결
            union(parents, a, b)
# 결과 리스트에 간선을 추가하여 경로에 간선 추가
            result_list.append(sorted_edges[i])
# 결과 리스트 반환
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

# 각각의 정점과 연결된 최상위 정점을 표시하기 위한 딕셔너리
parents={}
# 키값으로 각각의 정점을 넣고, value 값으로 해당 value의 key 정점과 같은 값을 넣는다.
# 예시) {'A':'A', 'B':'B', 'C':'C', 'D':'D'}
for i in stations:
    parents[i]=i

print(kruskal(stations, edges))

