import sys
from collections import deque
from collections import defaultdict
read = sys.stdin.readline


# 1000 ~ 9999 사이의 소수를 에라토스테네스의 체로 구함
def is_prime():
    for i in range(2, 101):
        for j in range(len(num)):
            if num[j] % i == 0:
                num[j] = 0
    return num

# 한자리 차이나는 애들의 리스트를 뱉는다
def one_diff(str):
    result = []
    for one in str_prime:
        diff = 0
        for i in range(4):
            if str[i] != one[i]:
                diff += 1
            if diff > 1: break
        if diff == 1:
            result.append(one)
    return result

# 한 자리씩 바꾼 것들을 덱에 담는다
def bfs(start, end):
    q = deque()
    visited = defaultdict(int)
    cnt = 1
    for one in one_diff(start):
        if one == end:
            return cnt
        else:
            q.append([one, cnt])
    visited[start] = 1
    while q:
        x = q.popleft()
        visited[x[0]] = 1
        next = one_diff(x[0])
        next = [i for i in next if visited[i] == 0]
        # if end in next:
        #     print(x[1]+1)
        #     break
        for one in next:
            if one == end:
                return x[1]+1
            else:
                visited[one] = 1
                q.append([one, x[1]+1])
        # print(q)



t = int(read())
num = [i for i in range(1003, 9998)]
is_prime()
prime = [one for one in num if one != 0]
str_prime = [str(one) for one in prime]
# print(prime)

for i in range(t):
    start, end = map(int, read().split())
    if start == end:
        print(0)
        continue
    else:
        print(bfs(str(start), str(end)))

