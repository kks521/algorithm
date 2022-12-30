def solution(left, right):
    nums = [x for x in range(left,right+1)]
    answer = 0
    for num in nums:
        if num ** (1/2) % 1 == 0:
            answer -= num
        else: 
            answer += num
    return answer