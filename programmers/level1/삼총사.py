def solution(number):
    answer = 0
    for n1 in range(len(number)-2):
        for n2 in range(n1+1,len(number)-1):
            for n3 in range(n2+1,len(number)):
                if number[n1] +  number[n2] +number[n3] == 0:
                    answer += 1
    return answer

solution([-3, -2, -1, 0, 1, 2, 3])