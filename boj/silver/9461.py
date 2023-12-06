#9461, silver3, dp

import sys 
cnt = int(sys.stdin.readline())
arr = [1,1,1,2,2]
for _ in range(cnt):
    num = int(sys.stdin.readline())
    if len(arr) < num:
        while len(arr) < num:
            arr.append(arr[-1]+arr[-5])
    print(arr[num-1])