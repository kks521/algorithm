import sys
n = int(sys.stdin.readline())
def solve(n):
        result = 0
        if n == 0:
            result = 0
        elif n == 1:
            result = 1
        elif n > 1:
            result = solve(n-2) + solve(n-1)
        return result 
print(solve(n))