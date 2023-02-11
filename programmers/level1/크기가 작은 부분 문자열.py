def solution(t, p):
    answer = 0
    cnt = len(t) - len(p) + 1 
    tnums = []
    for i in range(cnt):
        tnums.append(t[i:i+len(p)])
    for ts in tnums:
        if int(ts) <= int(p):
            answer += 1
    return answer