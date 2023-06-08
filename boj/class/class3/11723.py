import sys 
cnt = int(sys.stdin.readline())
s = set()
for i in range(cnt):
    operation = sys.stdin.readline().strip().split()
    if len(operation) == 1:
        if operation[0] == 'all': 
            s = set(x for x in range(1,21))
            continue
        else:
            s.clear()
            continue
    op, num = operation[0],operation[1]
    num = int(num)
    if op == 'add':
        s.add(num)
    elif op == 'remove':
        s.discard(num)
    elif op == 'check':
        if num in s:
            print(1)
        else: 
            print(0)
    elif op == 'toggle':
        if num not in s:
            s.add(num)
        else:
            s.discard(num)

