import sys
n = int(sys.stdin.readline())
nums = []
for i in range(n):
    nums.append(sys.stdin.readline().strip())
nums.sort(key=lambda x:(int(x.split()[0]),int(x.split()[1])))


for k in nums:
    print(k)