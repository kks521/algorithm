import sys 
a, b = map(int,sys.stdin.readline().split())
num1 = max(a,b)
num2 = min(a,b)
answer1 = 1 
for i in range(num2,1,-1):
    if num1 % i == 0 and num2 % i == 0:
        answer1 = i
        break
answer2 = int(num1 / answer1 * num2 / answer1 * answer1) 

print(f'{answer1}\n{answer2}')
