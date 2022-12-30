def solution(numbers):
    numList = [1,2,3,4,5,6,7,8,9,0]
    for num in numbers:
        numList.remove(num)
    answer = sum(numList)
    return answer

print(solution([1,2,3,4,6,7,8,0]))