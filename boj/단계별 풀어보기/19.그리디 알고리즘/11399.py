import sys 

n = int(sys.stdin.readline())
times = list(map(int,sys.stdin.readline().split()))
waitTime = 0 
ans = 0

times.sort()

for time in times:
    waitTime += time
    ans += waitTime

print(ans)
    