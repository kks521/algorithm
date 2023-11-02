import sys 
from collections import deque

n = int(sys.stdin.readline())
nums = deque(enumerate(map(int,sys.stdin.readline().split())))
ans = []

while nums:
    idx, num  = nums.popleft()
    ans.append(idx + 1)
    
    if num > 0: 
        nums.rotate(-(num - 1))
    elif num < 0:
        nums.rotate(-num)
    
print(' '.join(map(str,ans)))