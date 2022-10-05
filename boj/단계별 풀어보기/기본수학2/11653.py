import sys 
num = int(sys.stdin.readline())
if num == 1:
    pass
else:
    for i in range(2,num+1):
        while True:
            if num % i == 0:
                num = num / i 
                print(i)
            else:
                break