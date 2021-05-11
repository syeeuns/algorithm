
import sys
from collections import defaultdict
read = sys.stdin.readline

s = read().rstrip()
result = defaultdict(int)
temp = []
prev = ''
answer = ''

for i in range(len(s)):
    if 97 <= ord(s[i]) <= 122:
        if prev != '':
            num = int(''.join(temp))
            result[prev] += num
            temp = []
        prev = s[i]
    else:
        temp.append(s[i])

num = int(''.join(temp))
result[prev] += num

for k, v in result.items():
    answer += k + str(v)
print(answer)