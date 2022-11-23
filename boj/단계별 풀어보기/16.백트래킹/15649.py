import sys 

def solve(depth,n,m):
    if depth == m:
        print(' '.join(map(str,ans)))

    for i in range(1,n+1):
        if not checked[i]:
            checked[i] = True
            ans.append(i)
            solve(depth+1,n,m)
            checked[i] = False
            ans.pop()
n,m = map(int,sys.stdin.readline().split())
checked = [False] * (n+1)
ans = list()
solve(0,n,m)