import sys 
from collections import deque

cnt = int(sys.stdin.readline())
temp = deque()

for i in range(cnt):
    order = sys.stdin.readline().rstrip()
    if len(order) > 1:
        order = order.split()

    if order[0] == '1':
        temp.appendleft(order[-1])

    elif order[0] == '2':
        temp.append(order[-1])

    elif order[0] == '3':
        if temp:
            print(temp.popleft())
        else: 
            print(-1)

    elif order[0] == '4':
        if temp:
            print(temp.pop())
        else: 
            print(-1)
    
    elif order[0] == '5':
        print(len(temp))
    
    elif order[0] == '6':
        if temp:
            print(0)
        else: 
            print(1)

    elif order[0] == '7':
        if temp:
            print(temp[0])
        else: 
            print(-1)
    elif order == '8':
            if temp:
                print(temp[-1])
            else:
                print(-1)
                
    
    