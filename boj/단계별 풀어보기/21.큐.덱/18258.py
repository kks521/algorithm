import sys
from collections import deque
que = deque()
n = int(sys.stdin.readline())
for i in range(n):
    order  = sys.stdin.readline().rstrip()
    if 'push' in order:
        order = order.split()
        que.append(int(order[1]))
    elif order == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            print(que.popleft())
    elif order == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif order == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])
    elif order == 'size':
        print(len(que))
    elif order == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
            