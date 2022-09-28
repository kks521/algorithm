import sys

word = sys.stdin.readline().strip()
time = 0 
for i in word: 
    if i in 'PQRS':
        time += 8
    elif i in 'TUV':
        time += 9
    elif i in 'WXYZ':
        time +=10
    else:
        i = (ord(i) -59) // 3
        time += i + 1 
print(time)    