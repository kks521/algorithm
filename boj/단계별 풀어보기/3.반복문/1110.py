import sys 

n =int(sys.stdin.readline())
origin = n 
check = 0 

while True:
    n = int(n)
    if check > 0 and n == origin:
        print(check)
        break
    if len(str(n)) == 1: 
        n *= 11 
        check += 1  
        continue
    sum = int(n)//10 + int(n) % 10
    n = str(n)[-1] + str(sum)[-1]
    check += 1 