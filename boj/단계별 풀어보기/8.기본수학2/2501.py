import sys 
num1, num2 = map(int,sys.stdin.readline().split())
answer = []
for i in range(1,num1+1):
    if num1 % i == 0:
        answer.append(i)
if len(answer) < num2: 
    print(0)
else: 
    print(answer[num2-1])