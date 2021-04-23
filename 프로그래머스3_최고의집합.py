def solution(n, s):
    answer = []
    if n > s:
        answer.append(-1)
    else:
        mork = s // n
        namuji = s % n
        answer = [mork for _ in range(n)]
        if namuji:
            for i in range(namuji):
                answer[-1 - i] += 1
    return answer