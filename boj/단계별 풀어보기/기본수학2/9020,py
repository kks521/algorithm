import sys


primes = []
nums = [False,False] + [True] * 10000 
for i in range(2,10000):
    if nums[i]:
        primes.append(i)    
        for j in range(2*i,10000,i):
            nums[j] = False



case = int(sys.stdin.readline())
for i in range(case):
    n = int(sys.stdin.readline())
    a = n//2
    b = a
    for k in range(n):
        if a in primes and b in primes:
            print(a,b)
            break
        a-=1
        b+=1 
