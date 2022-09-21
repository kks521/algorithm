import sys
d1, d2, d3 = map(int,sys.stdin.readline().split())
prize = 0 
if d1 == d2 and d2 == d3:
    prize = d1 * 1000 + 10000
elif d1 != d2 and d1 != d3 and d2 != d3:
    prize = max([d1,d2,d3]) * 100 
elif d1 == d2 or d1 == d3: 
    prize = d1 * 100 + 1000
else: 
    prize = d2 * 100 + 1000 
    


print(prize)
 

