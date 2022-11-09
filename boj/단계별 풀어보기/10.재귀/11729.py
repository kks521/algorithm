import sys


def hanio(n,start,end):
    if n == 1: 
        print(start,end)    
        return
    hanio(n-1,start,6-start-end)
    print(start,end)
    hanio(n-1,6-start-end,end)

n = int(sys.stdin.readline())
print(2**n-1)
hanio(n,1,3)