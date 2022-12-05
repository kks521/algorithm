def solution(a, b):
    c = [n1 * n2 for n1,n2 in zip(a,b)]
    answer = sum(c)
    return answer