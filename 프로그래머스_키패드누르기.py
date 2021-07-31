def solution(numbers, hand):
    answer = ''
    right = 0
    left = 0
    for one in numbers:
        if one == 0: one = 10
        rest = one % 3
        if rest == 1:
            left = one
            answer += 'L'
        elif rest == 0:
            right = one
            answer += 'R'
        else:
            left_abs = abs(left - one)
            right_abs = abs(right - one)
            left_diff = left_abs //3 + left_abs % 3
            right_diff = right_abs // 3 + right_abs % 3
            if right_diff < left_diff:
                right = one
                answer += 'R'
            elif right_diff > left_diff:
                left = one
                answer += 'L'
            else:
                if hand == "right":
                    right = one
                    answer += 'R'
                else:
                    left = one
                    answer += 'L'
    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))

# 왼, 오의 바로 직전을 저장해둔다
# 자신만 누를수있는것이라면 바로 이동한다
# 가운데줄의 숫자라면, 차이가 더 작은 애가 누른다
# 차이가 같다면 hand에 따른다

