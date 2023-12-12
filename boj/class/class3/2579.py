#2579, 실버3, dp 
import sys 
cnt = int(sys.stdin.readline())
stair = [0] * 301
for _ in range(cnt):
    stair[_] = int(sys.stdin.readline())

ans = [0] * len(stair)

ans[0] = stair[0]
ans[1] = stair[0] + stair[1]
ans[2] = max(stair[0]+stair[2],stair[1]+stair[2])

for i in range(3,cnt):
    ans[i] = max(ans[i-3] + stair[i-1] + stair[i], ans[i-2]+ stair[i])

print(ans[cnt-1])