import time

def quick_sort (arr,key):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2][key]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        temp = num[key]
        if temp < pivot:
            lesser_arr.append(num)
        elif temp > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr,key) + equal_arr + quick_sort(greater_arr,key)

def Greedy (tuple):
    result = []
    sorted = quick_sort(tuple,1)
    result.append(sorted[0])
    for data in sorted:
        if data[0] >= result[-1][1]:
            result.append(data) 
    return result

class_list = [(4, 8), (3, 5), (2, 4), (1, 4), (8, 10), (6, 8), (5, 7), (4, 5), (5, 8), (9, 11)]

output = Greedy(class_list)

print(output)