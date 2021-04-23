# 40분
# 프로그래머스 사이트 네트워크 환경이 안좋아서 한 5~10분 까먹은듯

import sys
read = sys.stdin.readline
from collections import defaultdict


def solution(genres, plays):
    answer = []
    # (장르, 플레이수, 인덱스) 로 튜플 만들까?
    total = []
    for i in range(len(genres)):
        total.append((genres[i], plays[i], i))
    # 장르 순위 찾자
    genre_dict = defaultdict(list)
    for i in range(len(genres)):
        genre_dict[genres[i]].append((plays[i], i))
    genre_order = []
    for k, v in genre_dict.items():
        genre_dict[k].sort(key=lambda x: (-x[0], x[1]))
        sum = 0
        for i in range(len(v)):
            sum += v[i][0]
        genre_order.append((k, sum))
    genre_order.sort(key=lambda x: -x[1])
    print(genre_dict)
    print(genre_order)
    for one in genre_order:
        if len(genre_dict[one[0]]) == 1:
            answer.append(genre_dict[one[0]][0][1])
        else:
            answer.append(genre_dict[one[0]][0][1])
            answer.append(genre_dict[one[0]][1][1])
    return answer


genres = list(read().rstrip().split())
plays = list(map(int, read().split()))
print(solution(genres, plays))