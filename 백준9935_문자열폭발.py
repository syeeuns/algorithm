import sys
from collections import deque
read = sys.stdin.readline

string = deque(read().rstrip())
target = list(read().rstrip())

n = len(target)
temp = []

while len(string) != 0:
    temp.append(string.popleft())
    if temp[-n:] == target:
        for i in range(n):
            temp.pop()

if len(temp) != 0:
    print(''.join(list(temp)))
else:
    print('FRULA')


