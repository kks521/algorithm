#1406 실버2 스택 
import sys

temp = list(sys.stdin.readline().strip())
cnt = int(sys.stdin.readline())
temp2 = []
for _ in range(cnt):
    order = sys.stdin.readline().strip()

    if order == 'L':
        if temp:
            temp2.append(temp.pop())
    elif order == 'D':
        if temp2:
            temp.append(temp2.pop())
    elif order == 'B':
        if temp:
            temp.pop()
    else:
        temp.append(order[2])

temp.extend(reversed(temp2))
print(''.join(temp))