from collections import deque

def solution(priorities, location):
    answer = 0
    pri = deque()
    for i in range(len(priorities)):
        pri.append((priorities[i], i))

    while True:
        x = pri.popleft()
        # if pri:
        temp = sorted(pri, key=lambda y: -y[0])
        # print(temp)
        if pri and temp[0][0] > x[0]:
            pri.append(x)
        elif x[1] == location:
            answer += 1
            break
        else:
            answer += 1
    return answer