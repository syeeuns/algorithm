import sys
read = sys.stdin.readline

k, n = map(int, read().split())
lan = []
for i in range(k):
    lan.append(int(read()))

start = max(lan) // n
end = sum(lan) // n
answer = 0
while start <= end:
    mid = (start + end) // 2
    if mid == 0: mid = end
    cnt = 0
    for one in lan:
        cnt += one // mid
    if cnt >= n:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)