import sys 
from collections import deque
deque = deque()
n = int(sys.stdin.readline())
for i in range(n):
    order  = sys.stdin.readline().rstrip()
    if 'push' in order:
        order = order.split()
        if order [0] == 'push_front':
            deque.appendleft(int(order[1]))
        else: 
            deque.append(int(order[1]))
    elif order == 'pop_front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.popleft())
    elif order == 'pop_back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())
    elif order == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif order == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
    elif order == 'size':
        print(len(deque))
    elif order == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
