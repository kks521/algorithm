def solution(s):
    s = s.split(' ')    
    answer = []

    for i in s: 
        localAnswer = ''
        for j in range(len(i)):
            if j == 0 or j % 2 ==0:
                localAnswer += i[j].upper()
            else:
                localAnswer += i[j].lower()
        answer.append(localAnswer)
    answer = ' '.join(answer)    
    return answer
print(solution("try hello world"))