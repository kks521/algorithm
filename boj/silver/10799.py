# 10799 실버2 스택 
import sys 
temp = sys.stdin.readline().strip()
arr = []
ans = 0 
former = ''
for i in temp:
    if arr:
        if former == '(' and i == ')':
            arr.pop()
            ans += len(arr) 

        elif i == ')':
            arr.pop()
            ans += 1
        else: 
            arr.append(i) 
    else: 
        arr.append(i)
    former = i 
print(ans)