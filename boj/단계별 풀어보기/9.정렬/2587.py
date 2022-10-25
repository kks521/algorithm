from statistics import mean, median
import sys 
nums = []
for i in range(5):
    num = int(sys.stdin.readline())
    nums.append(num)
print(mean(nums))
print(median(nums))