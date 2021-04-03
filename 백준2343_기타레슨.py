# 전체합 ~ 가장 긴 레슨 시간
# 이분탐색

import sys
read = sys.stdin.readline

n, m = map(int, read().split())
lesson = list(map(int, read().split()))
left = max(lesson)
right = sum(lesson)
while left <= right:
    # mid값에 따른 블루레이 개수
    sum = 0
    cnt = 0
    mid = (left + right) // 2
    for i in range(len(lesson)):
        if sum + lesson[i] > mid:
            cnt += 1
            sum = 0
        sum += lesson[i]

    cnt += 1
    if cnt <= m:
        right = mid - 1
    else:
        left = mid + 1

print(left)
