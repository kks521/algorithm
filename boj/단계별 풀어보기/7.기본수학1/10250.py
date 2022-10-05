import sys
import math as m 
case = int(sys.stdin.readline())
for i in range(case):
    height, width, n = map(int,sys.stdin.readline().split())
    if n % height == 0: 
        y = height * 100 
    else:
        y = (n % height * 100) 
    x =  m.ceil(n / height) 
    print(y+x)