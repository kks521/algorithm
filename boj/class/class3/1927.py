#1927,silver2, heap 

import sys 
import heapq
n = int(sys.stdin.readline())
arr = [] 
for _ in range(n):
    order = int(sys.stdin.readline())
    if order > 0:
        heapq.heappush(arr,order)
    else: 
        if not arr:
            print(0)
        else:
            print(heapq.heappop(arr))
