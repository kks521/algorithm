import sys 

def euclid(a,b):
    r = a % b 
    if r == 0:
        return b
    return euclid(b,r)

num1, num2 = map(int,sys.stdin.readline().split())
if num1 < num2: 
    num1,num2 = num2, num1 
print( num1 * num2 // euclid(num1,num2))