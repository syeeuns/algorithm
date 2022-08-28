import sys
from collections import deque
read = sys.stdin.readline

string = list(read().rstrip())
m = int(read())
command = [read().split() for _ in range(m)]
pos1 = len(string)
# for one in command:
#     if one[0] == 'L' and pos != 0:
#         pos -= 1
#     elif one[0] == 'D' and pos != len(string):
#         pos += 1
#     elif one[0] == 'B' and pos != 0:
#         del string[pos - 1]
#     elif one[0] == 'P':
#         string.insert(pos, one[1])
#
# print(''.join(string))

rest = deque()
for one in command:
    if one[0] == 'L' and pos1 != 0:
        pos1 -= 1
        rest.appendleft(string.pop())
    elif one[0] == 'D' and pos1 != (len(string) + len(rest)):
        pos1 += 1
        string.append(rest.popleft())
    elif one[0] == 'B' and pos1 != 0:
        string.pop()
        pos1 -= 1
    elif one[0] == 'P':
        string.append(one[1])
        pos1 += 1

print(''.join(string + list(rest)))

#  a b c d
# 0 1 2 3 4
# 커서 위치 기준으로 스택을 2개 활용해보자