#2217, 실버4, 그리디 알고리즘

import sys 
n = int(sys.stdin.readline())
ropes = []

for _ in range(n):
    ropes.append(int(sys.stdin.readline()))
ropes.sort()
ans = 0 
for i in range(n):
    if ans < ropes[i] * (len(ropes)-i):
        ans = ropes[i] * (len(ropes)-i)

print(ans)