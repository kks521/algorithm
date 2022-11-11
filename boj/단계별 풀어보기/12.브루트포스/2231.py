import sys
n = int(sys.stdin.readline())
n2 = len(str(n)) * 9     
for i in range(n-n2,n):
    if i < 0: 
        continue
    result =  i + sum(list(map(int,list(str(i)))))
    if result == n:
        print(i)
        break
else:
    print(0)
