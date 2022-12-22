#16953, 실버2, 그리디 알고리즘

import sys 
ans = 1 
n, target = map(int,sys.stdin.readline().split())

while target >= n:
    if target == n:
        print(ans)
        break
    if target % 2 == 0:
        ans += 1
        target //= 2
    elif target % 10 == 1:
        target //= 10
        ans += 1 
    else: 
        print(-1)
        break
else:
    print(-1)

