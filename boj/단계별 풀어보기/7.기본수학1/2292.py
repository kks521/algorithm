import sys 

n = int(sys.stdin.readline())
line = 1
check = 0
while True: 
    line += check * 6 
    check += 1
    if n <= line:
        break
print(check)