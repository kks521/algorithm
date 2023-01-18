import sys 
n,m = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))
for i in range(n-1):
    nums[i+1] += nums[i]
for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    if a == 1: 
        print(nums[b-1])
        continue
    a,b = a-2,b-1
    print(nums[b] - nums[a])

# 5 4 3 2 1

# 5 9 12 14 15 