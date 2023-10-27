import sys 
nums = list(map(int,sys.stdin.readline().split()))
nums.sort()
numlimit = nums[0] + nums[1] -1 

if nums[2] > numlimit:
    nums[2] = numlimit
print(sum(nums))