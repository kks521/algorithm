def chang2(num,n):
    ans = []
    for i in num:
        s = ''
        for j in range(n-1,-1,-1):
            if i // 2**j == 0:
                s += '0'
            else:
                s += '1'
                i =  i - 2**j
        ans.append(s)
    return ans 
def solution(n, arr1, arr2):
    answer = []
    arr1 = chang2(arr1,n)
    arr2 = chang2(arr2,n)
    for a,b in zip(arr1,arr2):
        ans = ''
        for c,d in zip(a,b):
            if c == '1' or d == '1':
                ans += '1'
            else:
                ans+= '0' 
        ans = ans.replace('1','#')
        ans = ans.replace('0',' ')
        answer.append(ans)
    return answer


print(solution(	5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))