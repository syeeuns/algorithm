import sys
from collections import deque
from collections import defaultdict
read = sys.stdin.readline

s = int(read())
now = 1
clipboard = 0
depth = 0
q = deque()
q.append((now, clipboard, depth))
visited = defaultdict(int)
while q:
    x = q.popleft()
    y = str(x[0]) + str(x[1]) + str(x[2])
    if visited[y] == 1:
        continue
    visited[y] = 1

    if x[0] == s:
        print(x[2])
        q.clear()
        exit()
    else:
        # 클립보드 저장
        q.append((x[0], x[0], x[2]+1))
        # 붙여넣기
        if x[1] != 0:
            q.append((x[0]+x[1], x[1], x[2]+1))
        # 삭제
        if x[0] != 0:
            q.append((x[0]-1, x[1], x[2]+1))
