def solution(nums):
    answer = 0
    for n1 in range(len(nums)-2):
        for n2 in range(n1+1,len(nums)-1):
            for n3 in range(n2+1,len(nums)):
                if is_prime_number(nums[n1] + nums[n2] + nums[n3]):
                    answer += 1  
    return answer
def is_prime_number(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False 
    return True 

solution([1,2,3,4])

#