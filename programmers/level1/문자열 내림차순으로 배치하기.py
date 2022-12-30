def solution(s):
    s = reversed(sorted(s))
    return ''.join(s)

print(solution("Zbcdefg"))