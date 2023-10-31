import sys 
import math
cnt = int(sys.stdin.readline())
nums = [False,False] + [True] * 1000000
prime = []
for i in range(2,1000001):
               if nums[i]:
                prime.append(i)
                j = 2 
                while(i * j < 1000000):
                        nums[i*j] = False
                        j += 1

for _ in range(cnt):
        n = int(sys.stdin.readline())
        check = 0 
        for p in prime:
                if p > n: 
                        break
                if nums[n-p] and p <= n/2:
                        check += 1
        print(check)       
