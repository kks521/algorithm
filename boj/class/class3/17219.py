import sys

n, m = map(int,sys.stdin.readline().split())
passwords = []
ans = []

for i in range(n):
    passwords.append(sys.stdin.readline().split())

passwords = dict(passwords)

for k in range(m):
    search = sys.stdin.readline().rstrip()
    ans.append(passwords[search])
print('\n'.join(ans))