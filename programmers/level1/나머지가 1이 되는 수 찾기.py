def solution(n):
    x = n-1
    for i in range(2,n):
        if x % i == 0:
            answer = i
            break
    return answer