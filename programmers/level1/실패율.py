def solution(N, stages):
    answer = {}
    answer2 = []
    current_challenger = len(stages)
    for i in range(1,N+1):
        stage_challenger = stages.count(i)
        if current_challenger ==0:
            answer[i] = 0
            continue
        answer[i] = (stage_challenger/current_challenger)
        current_challenger -= stage_challenger
    sorted_keys = sorted(answer.items(),key= lambda x: x[1],reverse=True)
    for key,_ in sorted_keys:
        answer2.append(key)


    return answer2