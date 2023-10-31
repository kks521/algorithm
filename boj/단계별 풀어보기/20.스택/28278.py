import sys 
cnt = int(sys.stdin.readline())
temp =[]

for i in range(cnt):
    order = sys.stdin.readline().rstrip()
    if len(order) > 1:
        order = order.split()
    if order[0] == '1':
        temp.append(int(order[-1]))
    elif order[0] == '2':
        if temp:
            print(int(temp.pop()))
        else: 
            print(-1)
    elif order[0] == '3':
        print(len(temp))
    elif order[0] == '4':
        if temp:
            print(0)
        else: 
            print(1)
    elif order[0] == '5':
        if temp:
            print(temp[-1])
        else: 
            print(-1)