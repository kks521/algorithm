import sys
num1, num2 = map(int,sys.stdin.readline().split())
def alram(hour,min):
    min -= 45
    if min > 0:
        pass
    elif min < 0:
        hour -= 1  
        min = 60 + min  
        if hour == -1:
            hour = 23
    print(hour,min)        
alram(num1,num2)

