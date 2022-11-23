import sys
cnt, target = map(int, sys.stdin.readline().split())
coin = list()
ans = 0
for i in range(cnt):
    coin.append(int(sys.stdin.readline()))
coin.sort(reverse=True)
for j in coin:
    ans += target // j
    target %= j
print(ans)
