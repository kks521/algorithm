def solution(n, m):
    n,m = min(n,m),max(n,m)
    answer = []
    if m % n == 0:
        answer.extend([n,m])
    else:
        for i in range(n-1,0,-1):
            if n % i ==0 and m % i == 0:
                answer.append(i)
                break
        for j in range(2,n+1):
            if (j * m) % n == 0:
                answer.append(j*m)
                break
    

    return answer

print(solution(4,16))