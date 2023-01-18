def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        budget -= i 
        if budget < 0:
            break         
        answer += 1
    return answer

print(solution([2, 2, 3, 3], 10))