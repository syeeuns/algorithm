# 42분

from collections import deque


def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    else:
        visited = [False] * len(words)
        q = deque()
        depth = 0
        q.append((begin, depth))

        # not visited && 한글자 차이나는 애 찾기
        def pick(x):
            for i in range(len(words)):
                if not visited[i]:
                    diff = 0
                    for j in range(len(x[0])):
                        if x[0][j] != words[i][j]:
                            diff += 1
                        if diff > 1:
                            break
                    if diff == 1:
                        visited[i] = True
                        print(x[0], '->', words[i], x[1] + 1)
                        q.append((words[i], x[1] + 1))

        while q:
            x = q.popleft()
            pick(x)
            for one in q:
                if one[0] == target:
                    return one[1]

    return answer