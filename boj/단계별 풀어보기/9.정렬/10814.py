import sys
n = int(sys.stdin.readline())
nums = []
for i in range(n):
    nums.append(sys.stdin.readline().split())
nums.sort(key=lambda x:(int(x[0])))

for k in nums:
    print(' '.join(k))
    