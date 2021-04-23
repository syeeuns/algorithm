# 30분

def palindrome(target):
    if target == target[::-1]:
        return True
    else: 
        return False

def solution(s):
    answer = -1

    if s == s[::-1]:
        answer = len(s)
    else:
        length = len(s)
        for i in range(length):
            for j in range(i, length+1):
                if palindrome(s[i:j]):
                    answer = max(answer, len(s[i:j]))

    return answer