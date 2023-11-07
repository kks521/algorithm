import sys

def solve(num):
    if num ==1:
        return '-'
    left = solve(num//3)
    center = ' ' * (num//3)
    return left + center + left

while(1):
    try:
        n = 3 ** int(sys.stdin.readline())
        print(solve(n))
    except:
        break