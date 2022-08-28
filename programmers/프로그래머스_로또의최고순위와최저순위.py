def solution(lottos, win_nums):
    answer = []
    cnt = 0
    zero_cnt = lottos.count(0)
    for one in lottos:
        if one in win_nums:
            cnt += 1
    best = cnt + zero_cnt
    worst = cnt
    answer.append(rank(best))
    answer.append(rank(worst))
    return answer


def rank(num):
    if ((7 - num) >= 6):
        return 6
    else:
        return 7 - num


lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))


# for(lottos) :
# if i in win_nums
# 이걸로 일치하는 수 센다
# 일치하는 숫자가 최저등수
# 여기에 0의 갯수 더한게 최고등수

# 12분