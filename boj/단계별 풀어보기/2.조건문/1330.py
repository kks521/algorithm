import sys 
num1, num2 = map(int,sys.stdin.readline().split())
if num1 > num2:
    print(">")
elif num1 < num2:
    print("<")
elif num1 == num2:
    print("==") 
