def solution(nums):
    answer = 0
    cntnum = len(nums)//2
    nums = list(set(nums))
    if len(nums) >= cntnum:
        answer = cntnum
    else: 
        answer = len(nums) 
    return answer