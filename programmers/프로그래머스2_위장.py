from itertools import combinations
from collections import defaultdict

def solution(clothes):
    answer = 1
    fashion = defaultdict(list)
    for one in clothes:
        fashion[one[1]].append(one[0])
    arr = []
    key = fashion.keys()
    for one in key:
        answer *= len(fashion[one]) + 1


    return answer-1