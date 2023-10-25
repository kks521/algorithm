import sys 
while(1):

    num1 = int(sys.stdin.readline())
    if num1 == -1: 
        break 
    a = [ ]
    for i in range(1,num1):
        if num1 % i == 0:
            a.append(i)
    if num1 == sum(a):
        print(f'{num1} =',end=' ')
        for n in a: 
            if n == a[-1]:
                print(n)
            else:
                print(f'{n} +',end=' ')
    else:
        print(f'{num1} is NOT perfect.')
