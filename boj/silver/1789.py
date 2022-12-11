#1789, 실버5, 그리디 알고리즘

import sys 

n = int(sys.stdin.readline())
ans = 1
sumResult = 0
while True:
    if sumResult + ans > n:
        break
    sumResult += ans
    ans += 1 
print(ans - 1)    
