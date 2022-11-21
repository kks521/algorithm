import sys
s = sys.stdin.readline().rstrip()
ans = list()
for i in range(len(s)+1):
    cnt = 1 
    for j in range(len(s)-i):
        ans.append(s[cnt-1:cnt+i])
        cnt+=1 
print(len(set(ans)))