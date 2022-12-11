import sys 

n = int(sys.stdin.readline())

def factorial(n):
    if n == 0:
        return 1 
    return n * factorial(n-1)

n = factorial(n)
ans = 0
for i in str(n)[::-1]:
    if i != '0': 
        break
    ans += 1 

print(ans)