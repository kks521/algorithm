import sys
n = int(sys.stdin.readline())
nums = []
for i in range(n):
    nums.append(list(map(int,sys.stdin.readline().split())))
nums.sort(key=lambda x:(x[1],x[0]))
for k in nums:
    k = map(str,k)
    print(' '.join(k))