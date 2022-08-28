import sys, math
read = sys.stdin.readline

n, l = map(int, read().split())
woong = []
for _ in range(n):
    start, end = map(int, read().split())
    woong.append((start, end))

woong.sort()

start = 0
prev_end = 0
cnt = 0
for one in woong:
    start = max(prev_end, one[0])
    diff = math.ceil((one[1] - start) / l)
    prev_end = start + diff * l
    cnt += diff

print(cnt)

# 만약, 다음꺼의 시작점보다 더 갔다면, 이전의 끝점을 시작으로
# 다음꺼의 시작점보다 덜 갔다면, 다음꺼의 시작점을 시작점으로
# 풀이시간 13분