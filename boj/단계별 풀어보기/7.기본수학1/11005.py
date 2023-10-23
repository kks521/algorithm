import sys 
import math
n, b = map(int,sys.stdin.readline().split())
answer = ''
x = math.log(n,b)

for i in range(int(x),-1,-1):
    num = n // b**i
    n = n % b**i 
    if num > 9:
        answer += chr(num + 55)
    else: 
        answer += str(num)
print(answer)