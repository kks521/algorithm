def solution(answers):
    answer = []
    a = [1,2,3,4,5] * 2000
    b = [2,1,2,3,2,4,2,5] * 1250
    c = [3,3,1,1,2,2,4,4,5,5] * 1000
    scores = {'a':0,'b':0,'c':0}
    for cnt,i in enumerate(answers):
        if a[cnt] == i:
            scores['a'] += 1
        if b[cnt] == i:
            scores['b'] += 1             
        if c[cnt] == i:
            scores['c'] += 1
    score1 = scores['a']
    score2 = scores['b']
    score3 = scores['c']
    maxscore = max(score1,score2,score3)
    if score1 == maxscore:
        answer.append(1)
    if score2 == maxscore:
        answer.append(2)
    if score3 == maxscore:
        answer.append(3)        
    return answer
print(solution([1,2,3,4,5]	))