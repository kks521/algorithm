import sys 
num1 =int(sys.stdin.readline())
num2 =int(sys.stdin.readline())

if num1 > 0: 
    if num2 > 0: 
        print(1)
    else: 
        print(4)
else: 
    if num2 > 0: 
        print(2)
    else:
        print(3)                