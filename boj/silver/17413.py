#17413, 실버3, 스택
import sys 
s = sys.stdin.readline().rstrip()
temp = []
status = False

for i in s:
    if i == '>':
        temp.append(i)
        print(''.join(temp),end='')
        status = False
        temp.clear()
    elif i == '<':
        print(''.join(reversed(temp)),end='')
        temp.clear()
        status = True
        temp.append(i)
    elif i == ' ':
        if status:
            temp.append(i)
        else: 
            print("".join(reversed(temp)),end=' ')
            temp.clear()
    else: 
        temp.append(i)
print(''.join(reversed(temp)))
