def solution(a, b, n):
    current = n
    answer = 0
    while current >=a:
        answer += current // a * b 
        current = current % a + current // a * b    

    return answer
