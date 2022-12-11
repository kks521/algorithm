
def solution(number,limit,power):
    answer = 0
    def checkPower(num):
        cnt = 0
        for i in range(1,int(num**(1/2))+1):
            if num % i == 0:
                if i == num//i:
                    cnt += 1 
                else:
                    cnt += 2
        if cnt > limit:
            return power
        return cnt 
    
    for x in range(1,number+1):
        answer += checkPower(x)

    return answer
