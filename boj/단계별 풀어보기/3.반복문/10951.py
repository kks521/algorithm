import sys 
while True: 
    try:
        num1, num2 = map(int,sys.stdin.readline().split())
        print(num1+num2)
    except:
        break  