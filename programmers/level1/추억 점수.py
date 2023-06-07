def solution(name, yearning, photo):
    score = {}
    for n,y in zip(name,yearning):
        score[n] = y 
    answer = []
    for p in photo:
        current_score = 0 
        for p2 in p: 
            if p2 in score.keys():
                current_score += score[p2]
        answer.append(current_score)    
    return answer
solution(["may", "kein", "kain", "radi"],	[5, 10, 1, 3],	[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]	)