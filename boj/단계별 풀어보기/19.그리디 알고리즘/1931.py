import sys
cnt = int(sys.stdin.readline())
times = list()
ans = 0
for i in range(cnt):
    times.append(list(map(int, sys.stdin.readline().split())))
times.sort(key=lambda x: (x[1], x[0]))

last = 0
for s, l in times:
    if s >= last:
        ans += 1
        last = l
print(ans)
