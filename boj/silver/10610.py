#10610, 실버4, 그리디 알고리즘 

import sys 
n = sys.stdin.readline().rstrip()

if '0' not in n:
    print(-1)
else: 
    sum = 0 
    for i in n:
        sum += int(i)
    if sum % 3 != 0:
        print(-1)
    else: 
        n = sorted(n,reverse=True)
        print(''.join(n))  