import sys
num = int(sys.stdin.readline())
def solve(n):
    cnt = 99
    if n < 100:
        return print(n)
    for i in range(100,n+1):
        a = int(str(i)[0])
        b = int(str(i)[1])
        c = int(str(i)[2])  
        if a - b == b - c:
            cnt += 1 
    print(cnt)
solve(num)
