def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(len(computers[i])):
            if i != j:
                if computers[i][j] == 1:
                    graph[i].append(j)
    visited = [False] * n

    def dfs(graph, visited, start):
        visited[start] = True
        if graph[start] != []:
            for one in graph[start]:
                if not visited[one]:
                    dfs(graph, visited, one)

    # 컴포넌트 갯수 세기
    def dfsAll():
        component = 0
        for i in range(n):
            if not visited[i]:
                # 새로운 dfs 시작
                dfs(graph, visited, i)
                component += 1
        return component

    answer = dfsAll()
    return answer