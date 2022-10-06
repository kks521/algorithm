import sys



while True:
    m = int(sys.stdin.readline())
    n = 2* m
    primes =[]
    if n == 0: 
        break
    nums = [False,False] + [True] * n 
    for i in range(2,n+1):
        if nums[i]:
            for j in range(2*i,n+1,i):
                nums[j] = False
    for k in range(m+1,n+1):
        if nums[k]:
            primes.append(k)
    print(len(primes))
        