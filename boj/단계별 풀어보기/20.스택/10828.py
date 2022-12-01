import sys
stack = list()
n = int(sys.stdin.readline())
for i in range(n):
    order  = sys.stdin.readline().rstrip()
    if 'push' in order:
        order = order.split()
        stack.append(int(order[1]))
    elif order == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif order == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
            