import sys
from collections import deque
read = sys.stdin.readline

n, m = map(int, read().split())
war = [list(read().rstrip()) for _ in range(m)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[0 for _ in range(n)] for _ in range(m)]

def bfs(x ,y, target):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and war[nx][ny] == target and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1
    return cnt


my_power = 0
enemy_power = 0
for i in range(m):
    for j in range(n):
        if war[i][j] == 'W' and not visited[i][j]:
            my_power += (bfs(i, j, 'W')) ** 2
        elif war[i][j] == 'B' and not visited[i][j]:
            enemy_power += (bfs(i, j, 'B')) ** 2

print(my_power, enemy_power)
# bfs로 붙어있는 애들 check
# 덩어리^2
