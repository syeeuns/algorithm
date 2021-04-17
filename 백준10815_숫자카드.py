import sys
read = sys.stdin.readline

# 이분탐색
n = int(read())
have = sorted(list(map(int, read().split())))
m = int(read())
ques = list(map(int, read().split()))

start = 0
end = n-1

for one in ques:
    flag = False
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if have[mid] > one:
            end = mid - 1
        elif have[mid] < one:
            start = mid + 1
        else:
            print(1, end=' ')
            flag = True
            break
    if flag == False:
        print(0, end=' ')



# -10 2 3 6 10



