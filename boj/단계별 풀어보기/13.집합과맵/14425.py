import sys 
n,m = map(int,sys.stdin.readline().split())
words = list()
cnt = 0 
for i in range(n+m):
    words.append(sys.stdin.readline().rstrip())
keys = set(words[:n])
for j in words[n:]:
    if j in keys:
        cnt += 1 
print(cnt)