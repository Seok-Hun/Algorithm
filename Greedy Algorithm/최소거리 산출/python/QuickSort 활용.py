# Quick Sort 알고리즘으로 정렬한 후 각각의 최소 거리를 더하였다.

# 시간측정용 time 모듈
import time

# Quick Sort 함수
# input : 정렬되지 않은 배열
# output : 오름차순으로 정렬된 배열
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

# Greedy Algorithm 구현
# input : 여러 경로들의 리스트를 담은 리스트
# output : 최적 경로를 계산한 거리값
def Greedy(arr_list):
  result = 0
  for arr in arr_list:
    sorted_arr = quick_sort(arr)
    result += sorted_arr[0]
  return result

Gac_Dae = [190, 150, 180]
Dae_Bus = [230, 170, 220]

output = Greedy([Gac_Dae, Dae_Bus])

print(output)