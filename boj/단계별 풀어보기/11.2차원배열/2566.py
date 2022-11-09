import sys
nums = []
maxs = []
for i in range(9):
    nums.append(list(map(int,sys.stdin.readline().split())))
for i in range(9):
    maxs.append(max(nums[i]))
a = maxs.index(max(maxs))
b = nums[a] 
c = nums[a].index(max(maxs))
print(max(maxs))
print(a+1,c+1)