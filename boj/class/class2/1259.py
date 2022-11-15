import sys
while True:
    n = sys.stdin.readline().strip()
    if n == '0': 
        break
    else: 
        if n == ''.join(reversed(n)):
            print('yes')
        else: 
            print('no')