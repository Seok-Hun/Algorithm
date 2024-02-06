import heapq

# G : 그래프, start : 시작 정점, end : 목표 정점
def dijkstra(G, start, end):
# 그래프 딕셔너리의 키값을 똑같이 가지는 distances 딕셔너리 선언, 모든 value 값은 양의 무한으로 초기화
# 해당 딕셔너리는 시작 정점에서 각 정점까지의 거리를 나타내는 용도
    distances = {node:float('inf') for node in G}
# 목표 정점까지의 경로 탐색을 위해 이전 정점들을 저장할 딕셔너리 선언, 모든 value 값은 0으로 초기화
    parents = {i:0 for i in G}
# 경로를 저장하기 위한 path 선언, 빈 리스트로 초기화
    path = []
# 시작 정점부터 시작 정점까지의 거리는 0이므로 시작 정점까지의 거리는 0 으로 초기화
    distances[start] = 0
# 이전 정점들을 저장할 큐
    queue = []
# heappush로 시작 정점까지의 거리와 시작 정점을 큐에 추가
    heapq.heappush(queue, [distances[start],start])

# queue가 빈 리스트([])가 될 때까지 반복문 수행
    while queue:
# currentDistance : 큐에 저장된 시작 정점부터 이전 정점까지의 길이
# currentDestination : 큐에 저장된 이전 정점
# heappop은 힙에서 최소값을 반환하는 동시에 삭제하는 역할을 한다.
        currentDistance,currentDestination = heapq.heappop(queue)
# 이전 정점까지의 현재 거리가 이전 정점까지의 거리보다 작다면 반복문을 건너뛴다.
# 최소 거리를 구하는 것이 목표이므로 현재 거리가 이전 거리보다 더 가깝다면 굳이 계산을 더 할 필요가 없다.
# 반복문을 건너뛰므로 힙이 줄어들기만 하는 효과가 있다.
        if distances[currentDestination] < currentDistance:
            continue
# adjacent : 이전 정점에 해당하는 그래프의 정점과 인접한 정점
# weight : 이전 정점에 해당하는 그래프의 정점과 그 정점에 인접한 정점간의 거리(간선의 가중치)
# 이전 정점에 해당하는 그래프의 정점과 인접한 정점들까지의 거리를 모두 계산할 예정이다.
        for adjacent, weight in G[currentDestination].items():
# distance : 시작 정점부터 이전 정점 사이까지의 거리와 weight를 합친 시작 지점부터 현재 정점까지의 거리
            distance = currentDistance + weight
# 만약 계산한 현재 정점까지의 거리가 기존에 저장되어 있던 현재 정점까지의 거리보다 작다면
            if distance < distances[adjacent]:
# 기존에 저장되어 있던 현재 정점까지의 거리를 방금 계산한 현재 정점까지의 거리로 갱신
                distances[adjacent] = distance
# 최소 거리의 갱신이 발생한 것이므로 현재 정점과 인접한 이전 정점을 value 값으로 저장
# 키값에는 각각의 정점이 할당
# value에는 시작 정점과 키값에 해당하는 정점까지의 경로를 연결했을 때 키값 정점의 바로 이전 정점이 할당된다.
                parents[adjacent] = currentDestination
# 힙에 현재 정점(갱신이 발생한 정점)과 해당 정점까지의 거리를 추가
                heapq.heappush(queue, [distance, adjacent])

# while문을 탈출하면 최단 경로는 distances에 딕셔너리 형태로 저장되어 있다.

# 경로를 탐색하기 위한 반복문
# end가 0이 될 때까지 반복한다.
    while end:
# 경로 리스트에 end에 해당하는 정점을 추가한다.
        path.append(end)
# end 값을 end에 해당하는 정점 이전 정점으로 변경한다.
        end = parents[end]
# 시작 정점에 해당하는 키값의 value는 변하지 않는다.
# parents의 value를 0으로 초기화했기 때문에 end가 0이라는 의미는 시작 정점부터 목표 정점까지 역순으로 경로를 모두 살펴보았다는 의미이다.
# path를 역순으로 보면 시작 정점부터 목표 정점까지의 경로를 나타낸다.
    return path[::-1]

stations = {
    'A': {'B': 3, 'C': 2},
    'B': {'D': 7, 'E': 8},
    'C': {'A': 2, 'D': 4, 'E':1},
    'D': {'B': 7, 'C': 4},
    'E': {'B': 8, 'C': 1}
}

print(dijkstra(stations, 'E', 'A'))