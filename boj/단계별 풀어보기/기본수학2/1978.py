import sys
case = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
check = []
prime = []
cnt = 0
for i in range(2,max(nums)+1):
    if i not in check: 
        prime.append(i)
        for j in range(max(nums)//i+1):
            check.append(i*j)
for k in nums: 
    if k in prime:
        cnt += 1 


print(cnt) 

