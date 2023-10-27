import sys 
maxX = -10000
minX = 10000
maxY = -10000
minY = 10000

cnt = int(sys.stdin.readline())

for i in range(cnt):
    num1, num2 = map(int,sys.stdin.readline().split())
    if num1 > maxX:
        maxX = num1 
    if num1 < minX:
        minX = num1 
    if num2 > maxY:
        maxY = num2
    if num2 < minY:
        minY = num2

if maxX == minX or maxY == minY: 
    print(0)
else: 
    answer = (maxX - minX) * (maxY - minY)
    print(answer)