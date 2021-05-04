from collections import defaultdict

arr = [4,6,0,2,1,4,5,7,9,4,2,1,4,6,4,7,9,3,2,1,3,5,6,78,8,9,6,4,2,434,67,6,84,3,31,2,24,67,1,23,4]
# arr = [7,2,4,1,9]

# O(n^2)
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(1, n-i):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]


# O(n^2)
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        # 들어갈 자리가 i
        minimum = 9999999
        idx = 0
        for j in range(i, n):
            if minimum > arr[j]:
                minimum = arr[j]
                idx = j
        arr[i], arr[idx] = minimum, arr[i]


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


def countingSort(arr):
    n = len(arr)
    maxi = max(arr)
    result = []
    counting = [0 for _ in range(maxi+1)]
    for i in range(n):
        counting[arr[i]] += 1

    for i in range(maxi+1):
        for _ in range(counting[i]):
            result.append(i)
    return result


# 항상 O(n*logn)
n = len(arr)
sortedList = [0 for _ in range(n)]
def merge(arr, m, mid, n):
    global sortedList
    i, k = m, m
    j = mid+1

    while i <= mid and j <= n:
        if arr[i] <= arr[j]:
            sortedList[k] = arr[i]
            i += 1
        else:
            sortedList[k] = arr[j]
            j += 1
        k += 1

    if i > mid: # i가 넘어가면 j 쪽에 남은 걸 마저 담아줘야함
        while j <= n:
            sortedList[k] = arr[j]
            j += 1
            k += 1

    elif j > n:
        while i <= mid:
            sortedList[k] = arr[i]
            i += 1
            k += 1

    for t in range(m, n+1):
        arr[t] = sortedList[t]


def mergeSort(arr, m, n):
    if m < n:
        mid = (m + n) // 2
        mergeSort(arr, m, mid)
        mergeSort(arr, mid+1, n)
        merge(arr, m, mid, n)


# bubbleSort(arr)
# selectionSort(arr)
# insertionSort(arr)
# print(countingSort(arr))
mergeSort(arr, 0, len(arr)-1)
print(arr)

