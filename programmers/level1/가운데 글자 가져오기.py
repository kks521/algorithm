def solution(s):
    if len(s) % 2 == 1:
        return s[len(s)//2]
    else:
        a = len(s)/2
        return s[len(s)//2-1:len(s)//2+1]
print(solution('abcde'))