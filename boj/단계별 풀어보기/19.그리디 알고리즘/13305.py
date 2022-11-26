
import sys
# 58점 코드
'''
n = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().split()))
oilPrice = list(map(int, sys.stdin.readline().split()))[:-1]
minPrice = min(oilPrice)
ans = 0
cnt = 0
check = 0
for i in range(n-1):
    i += check
    if i >= n - 1:
        break
    cnt = 1
    for j in oilPrice[i+1:]:
        if j < oilPrice[i]:
            break
        cnt += 1
    ans += oilPrice[i] * sum(distance[i:i+cnt])
    check += cnt - 1
print(ans)
'''
n = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().split()))
oilPrice = list(map(int, sys.stdin.readline().split()))
minPrice = oilPrice[0]
ans = oilPrice[0] * distance[0]
for i in range(1, n-1):
    if minPrice > oilPrice[i]:
        minPrice = oilPrice[i]
    ans += minPrice * distance[i]
print(ans)
