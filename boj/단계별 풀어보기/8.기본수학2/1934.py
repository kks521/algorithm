import sys 

cnt = int(sys.stdin.readline())

def euclid(a,b):
    r = a % b 
    if r == 0:
        return b
    return euclid(b,r)

for i in range(cnt):
    num1, num2 = map(int,sys.stdin.readline().split())
    if num1 < num2: 
        num1,num2 = num2, num1 
    print( num1 * num2 // euclid(num1,num2))