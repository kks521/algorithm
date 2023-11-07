import sys 

n  = int(sys.stdin.readline())

def solve(num):
    if num == 0:
        return 1
    return num * solve(num -1)

print(solve(n))