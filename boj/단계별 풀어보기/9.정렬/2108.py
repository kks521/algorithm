import sys
from typing import Counter
n = int(sys.stdin.readline())
nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline()))
nums.sort()
cnt = Counter(nums).most_common(2)

print(round(sum(nums)/n))    
print(nums[n//2])
if len(nums) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(nums[-1]-nums[0])