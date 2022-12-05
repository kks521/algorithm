import sys 
n = int(sys.stdin.readline())
stack = []
ans = []
cnt =1 
status = True
for i in range(n):
    check = int(sys.stdin.readline())
    while cnt <= check:
        stack.append(cnt)
        ans.append('+')
        cnt += 1

    if check == stack[-1]:
        stack.pop()
        ans.append('-')
    else:
        status = False
        break
if status:
    print('\n'.join(ans))
else: 
    print('NO')        
    