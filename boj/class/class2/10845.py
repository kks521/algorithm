import sys 
from collections import deque

cnt = int(sys.stdin.readline())
temp = deque()

for _ in range(cnt):
    order = sys.stdin.readline().rstrip().split()
    
    if order[0] == 'push':
        temp.append(int(order[1]))
    
    if order[0] == 'pop':
        if temp:
            print(temp.popleft())
        else:
            print(-1)

    if order[0] == 'size':
        print(len(temp))

    if order[0] == 'empty':
        if temp:
            print(0)
        else:
            print(1)

    if order[0] == 'front':
        if temp:
            print(temp[0])
        else:
            print(-1)

    if order[0] == 'back':
        if temp:
            print(temp[-1])
        else:
            print(-1)
    


            
    

    