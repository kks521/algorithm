#1026, 실버4, 그리디 알고리즘

import sys 

n = int(sys.stdin.readline())
numsA = list(map(int,sys.stdin.readline().split()))
numsB = list(map(int,sys.stdin.readline().split()))
ans = 0

for i in range(n):
    maxNum = max(numsB)
    minNum = min(numsA)
    ans += maxNum * minNum
    numsA.remove(minNum)
    numsB.remove(maxNum)
print(ans)
