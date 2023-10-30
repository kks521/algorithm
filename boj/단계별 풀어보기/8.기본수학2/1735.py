import sys 

def euclid(a,b):
    r = a % b 
    if r == 0:
        return b
    return euclid(b,r)

a, b = map(int,sys.stdin.readline().split())
c, d = map(int,sys.stdin.readline().split())


denominator = b * d // (euclid(b,d))
numerator = a * denominator // b +  c * denominator // d 

temp = euclid(denominator, numerator)

if temp > 1:
    denominator //= temp 
    numerator //= temp

print(numerator, denominator)