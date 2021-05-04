arr = [4,6,0,2,1,4,5,7,9,4,2,1,4,6,4,7,9,3,2,1,3,5,6,78,8,9,6,4,2,434,67,6,84,3,31,2,24,67,1,23,4]
# arr = [7,2,4,1,9]


# 최선의 경우 : O(n), 평균과 최악의 경우 : O(n^2)
def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        prev = i - 1
        while prev >= 0 and temp < arr[prev]:
            arr[prev+1] = arr[prev]
            prev -= 1

        arr[prev+1] = temp


insertionSort(arr)
print(arr)