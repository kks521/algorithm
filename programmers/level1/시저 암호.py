def solution(s, n):
    answer = []

    for i in s:        
        target = ord(i) + n 
        if i == ' ':
            answer.append(' ')
        elif ord(i) > 90:
            if target > 122:
                target -= 26
                answer.append(chr(target))
            else:
                answer.append(chr(target))
        else:
            arget = ord(i) + n 
            if target > 90:
                target -= 26
                answer.append(chr(target))
            else:
                answer.append(chr(target))
    answer = ''.join(answer)
    return answer

solution("a B z",4)