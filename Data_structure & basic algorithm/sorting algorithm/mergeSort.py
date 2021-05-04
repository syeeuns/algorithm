arr = [4,6,0,2,1,4,5,7,9,4,2,1,4,6,4,7,9,3,2,1,3,5,6,78,8,9,6,4,2,434,67,6,84,3,31,2,24,67,1,23,4]
# arr = [7,2,4,1,9]


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


mergeSort(arr, 0, len(arr)-1)
print(arr)