import sys
from itertools import combinations
read = sys.stdin.readline

t = int(read())
for i in range(t):
    n = int(read())
    mbti = list(read().split())
    if n > 32:
        print(0)
        continue
    else:
        cand = list(combinations(mbti, 3))
        score = []
        for one in cand:
            temp = 0
            candi = list(combinations(one, 2))
            for couple in candi:
                person1 = couple[0]
                person2 = couple[1]
                for j in range(4):
                    if person1[j] != person2[j]: temp += 1
            score.append(temp)
    print(min(score))