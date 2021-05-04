arr = [4,6,0,2,1,4,5,7,9,4,2,1,4,6,4,7,9,3,2,1,3,5,6,78,8,9,6,4,2,434,67,6,84,3,31,2,24,67,1,23,4]
# arr = [7,2,4,1,9]

# 최선의 경우 O(n*logn)
# 최악의 경우 O(n^2)

# 피벗 기준으로 왼쪽에는 작은 값, 오른쪽에는 큰 값이 들어가도록 자리를 바꿈
def qsort(arr, start, end):
    mid = (start + end) // 2
    pivotVal = arr[mid]
    leftPtr = start
    rightPtr = end

    if len(arr) == 1: return 0

    while leftPtr <= rightPtr:
        while arr[leftPtr] < pivotVal:
            leftPtr += 1
        while arr[rightPtr] > pivotVal:
            rightPtr -= 1
        if leftPtr <= rightPtr:
            arr[leftPtr], arr[rightPtr] = arr[rightPtr], arr[leftPtr]
            leftPtr += 1
            rightPtr -= 1

    # while문 나올때는 항상 두 ptr이 엇갈리거나 같은 상태니까
    # start ---- rightPtr  leftPtr ---- end
    # 이런 상태로 존재하겠지
    if start < rightPtr:
        qsort(arr, start, rightPtr)
    if leftPtr < end:
        qsort(arr, leftPtr, end)

def quickSort(arr,):
    qsort(arr, 0, len(arr) - 1)

quickSort(arr)
print(arr)