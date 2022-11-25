import sys
expression = sys.stdin.readline().rstrip().split('-')
ans = 0
if expression[0].isdigit():
    ans += int(expression[0])
else:
    firstNum = expression[0].split('+')
    ans += sum(map(int, firstNum))

for i in expression[1:]:
    if i.isdigit() == True:
        ans -= int(i)
        continue
    s = i.split('+')
    ans -= sum(map(int, s))

print(ans)
