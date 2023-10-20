import sys 

n, m = map(int,sys.stdin.readline().split())
baskets = [x for x in range(1,n+1)]

for i in range(m):
    num1, num2 = map(int,sys.stdin.readline().split())
    baskets[num1-1], baskets[num2-1] = baskets[num2-1] ,baskets[num1-1]

print(*baskets)

