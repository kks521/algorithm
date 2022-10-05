import sys
m, n = map(int,sys.stdin.readline().split())

def isprime(n):
    if n == 1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return False
        return True 

for i in range(m,n+1):
    if isprime(i):
        print(i)