def solution(price, money, count):
    total = count*(2*price +(count-1)*price)/2
    answer = money - total 
    if answer >= 0: 
        return 0
    else: 
        return answer * -1
