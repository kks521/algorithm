import sys 

a, b = map(int,sys.stdin.readline().split())
c = int(sys.stdin.readline())
n = int(sys.stdin.readline()) 

def fn(num):
    return a * num + b   

if a <= c and c * n >= fn(n):     
    print(1)
else: 
    print(0)      

