import sys
import math 

cnt = int(sys.stdin.readline())
nums = []

for _ in range(cnt):
    nums.append(int(sys.stdin.readline()))

def is_prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True


for n in nums: 
    while(1):
        if is_prime(n):
            print(n)
            break
        else: 
            n += 1
