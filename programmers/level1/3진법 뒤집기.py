def solution(n):
    answer = []
    answer2 = 0
    while n > 0:
        answer.append(n%3)
        n = n // 3
    for index,num in enumerate(answer[::-1]):
        answer2+=3**index*num
    return answer2
print(solution(45))