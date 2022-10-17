import sys
n = int(sys.stdin.readline())
nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline()))
for j in sorted(nums):
    print(j) 