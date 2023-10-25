import sys 
while(1):
    num1, num2 =  map(int,sys.stdin.readline().split())
    if num1 == 0 and num2 == 0: 
            break 
    if num1 % num2 == 0 or num2 % num1 == 0: 
        if num1 > num2: 
            print('multiple')
        else:
            print('factor')
    else:
        print('neither')