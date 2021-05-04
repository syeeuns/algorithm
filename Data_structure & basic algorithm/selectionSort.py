arr = [4,6,0,2,1,4,5,7,9,4,2,1,4,6,4,7,9,3,2,1,3,5,6,78,8,9,6,4,2,434,67,6,84,3,31,2,24,67,1,23,4]
# arr = [7,2,4,1,9]

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


selectionSort(arr)
print(arr)