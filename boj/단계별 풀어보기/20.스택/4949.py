import sys 
while True:
    str = input()
    if str == '.':
        break
    if not any(s1 in str for s1 in ['[',']','(',')']):
        print('yes')
        continue
    stack = []
    for s in str:
        if s == '[' or s == '(':
            stack.append(s)
        elif s == ')':
            if len(stack) > 0 and stack[-1] == '(' :
                stack.pop()
            else: 
                stack.append(s)
        elif s == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else: 
                stack.append(s)
    if stack:
        print('no')
    else: 
        print('yes')