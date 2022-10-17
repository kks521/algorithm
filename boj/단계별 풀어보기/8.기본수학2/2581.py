import sys 
m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
check = []
prime = []
result = []
for i in range(2,n+1):
    if i not in check: 
        prime.append(i)
        if not (i % 2 ==0 and i != 2): 
            for j in range(n//i+1):
                check.append(i*j)
for k in range(m,n+1):
    if k in prime:
        result.append(k)
if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))

