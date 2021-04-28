arr = [4,6,2,1,4,5,7,9,4,2,1,4,6,4,7,9,0,3,2,1,3,5,6,78,8,9,6,4,2,434,67,6,84,3,31,2,24,67,1,23,4]

def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


