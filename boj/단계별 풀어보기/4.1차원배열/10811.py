import sys 
n,m = map(int,sys.stdin.readline().split())

baskets = [x for x in range(1,n+1)]

for i in range(m):
    num1, num2 = map(int,sys.stdin.readline().split())
    reversedorder = list(reversed(baskets[num1-1:num2]))
    n = 0 
    for j in range(num1-1,num2):
        baskets[j] = reversedorder[n]
        n += 1
    
print(*baskets)