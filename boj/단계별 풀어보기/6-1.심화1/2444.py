import sys
n = int(sys.stdin.readline())
for i in range(n):
    star = (1+2*i) * '*'
    space = (n - 1 - i) *' '
    print(f'{space}{star}')
for j in range(n-2,-1,-1):
    star = (1+2*j) * '*'
    space = (n - 1 - j) *' '
    print(f'{space}{star}')

