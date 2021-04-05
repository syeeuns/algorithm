import sys
read = sys.stdin.readline

node = int(read())
line = int(read())
graph = [[] for _ in range(node+1)]
visited = [False for _ in range(node+1)]
cnt = 0
for i in range(line):
    start, end = map(int, read().split())
    graph[start].append(end)
    graph[end].append(start)


def dfs(graph, v, visited):
    global cnt
    visited[v] = True
    cnt += 1
    for one in graph[v]:
        if not visited[one]:
            dfs(graph, one, visited)

dfs(graph, 1, visited)
print(cnt-1)