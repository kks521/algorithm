def solution(k, m, score):
    answer = 0 
    score.sort(reverse=True)
    for i in range(len(score)//m):
        current_box = score[i*m:(i+1)*m]        
        answer += current_box[m-1]*m
    return answer

