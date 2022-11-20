import sys
n, m = map(int,sys.stdin.readline().split())
nl = set()
ans = list()
for i in range(n):
    nl.add(sys.stdin.readline().rstrip())
for i in range(m):
    name = sys.stdin.readline().rstrip() 
    if name in nl:
        ans.append(name)
print(len(ans))
print('\n'.join(sorted(ans)))


