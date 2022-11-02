import sys
n = int(sys.stdin.readline())
def solve(n):
    result = 1 
    if n > 0:
        result = n * solve(n-1)
    return result
print(solve(n))