# itertools 사용 풀이
# import sys
# from itertools import combinations
# read = sys.stdin.readline
#
# while True:
#     arr = list(map(int, read().split()))
#     if arr[0] == 0:
#         break
#     else:
#         k = arr[0]
#         combination = combinations(arr[1:], 6)
#         for one in combination:
#             for i in one:
#                 print(i, end=' ')
#             print()
#         print()

# dfs 풀이
import sys
read = sys.stdin.readline

def dfs(start, depth):
    if depth == 6:
        for i in range(k):
            if check[i]:
                print(arr[i], end=' ')
        print()
    for i in range(start, k):
        check[i] = True
        dfs(i+1, depth+1)
        check[i] = False


while True:
    arr = list(map(int, read().split()))
    if arr[0] == 0:
        break
    else:
        k = arr[0]
        arr = arr[1:]
        check = [False] * k
        dfs(0, 0)
        print()

