def solution(x):
    answer = x % sum(list(map(int,str(x)))) == 0 
    return answer