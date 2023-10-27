import sys  
n = int(sys.stdin.readline())
ans = 0
a  = list(range(1,n-1))
b = list(reversed(a))
for i in range(n-2):
    ans += a[i] * b[i]
print(ans)
print(3)
