import sys
read = sys.stdin.readline

n = int(read())
initial = list(read().rstrip())
num = []

for i in range(len(initial)):
    if 48 <= ord(initial[i]) <= 57:
        num.append(initial[i])
    elif i > 0 and 48 <= ord(initial[i-1]) <= 57:
        num.append('-')

num = ''.join(num).split('-')
result = 0
for one in num:
    if one != '':
        result += int(one)

print(result)