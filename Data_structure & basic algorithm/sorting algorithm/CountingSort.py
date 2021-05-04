arr = [4,6,0,2,1,4,5,7,9,4,2,1,4,6,4,7,9,3,2,1,3,5,6,78,8,9,6,4,2,434,67,6,84,3,31,2,24,67,1,23,4]
# arr = [7,2,4,1,9]


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


print(countingSort(arr))
