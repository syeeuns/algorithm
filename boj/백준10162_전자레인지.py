import sys
read = sys.stdin.readline

# 풀이시간 : 10분
# 전자레인지 시간 300초 60초 10초
n = int(read())
if n % 10:
    print(-1)
else:
    time = [300, 60, 10]
    answer = []
    while n >= 10:
        for one in time:
            if n >= one:
                answer.append(n//one)
                n %= one
            else:
                answer.append(0)

    print(*answer)