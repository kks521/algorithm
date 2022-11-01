import sys
from tabnanny import check
n = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
qw = {}
set_nums = sorted(list(set(nums)))
check = 0 
for i in set_nums:
    qw[i] = check
    check += 1 
for k in nums:
    print(qw[k],end=' ')