def solution(s):
    answer = []
    for inum,i in enumerate(s): 
        for jnum, j in zip(range(0,inum),s[:inum][::-1]):

            if j == i: 
                answer.append(jnum+1)
                break
        if inum + 1 > len(answer):
            answer.append(-1)

    return answer
solution("banana")