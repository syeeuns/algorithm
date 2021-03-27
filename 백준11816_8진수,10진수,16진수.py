import sys
read = sys.stdin.readline

n = read().rstrip()[::-1]
result = 0

if (n.endswith("x0")):
    n = list(n[:-2])
    for i in range(len(n)):
        if n[i] == 'a':
            n[i] = 10
        elif n[i] == 'b':
            n[i] = 11
        elif n[i] == 'c':
            n[i] = 12
        elif n[i] == 'd':
            n[i] = 13
        elif n[i] == 'e':
            n[i] = 14
        elif n[i] == 'f':
            n[i] = 15
        else:
            n[i] = int(n[i])
        result += n[i] * (16**i)
    print(result)

elif(n.endswith("0")):
    n = list(map(int, n[:-1]))
    for i in range(len(n)):
        result += n[i] * (8**i)
    print(result)

else:
    print(n[::-1])