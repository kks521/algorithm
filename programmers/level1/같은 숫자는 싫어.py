def solution(arr):
    answer = []
    lastNum = 10
    for i in arr:
        if i == lastNum:
            continue
        answer.append(i)
        lastNum = i 
    return answer
print(solution([1, 1, 3, 3, 0, 1, 1]))