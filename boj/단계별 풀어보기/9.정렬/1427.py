import sys
n = sys.stdin.readline().strip()
nums = []
for i in n:
    nums.append(int(i))
nums.sort(reverse=True)
for j in nums:
    print(j,end='')
    

