import sys 

basketNum, cnt = map(int, sys.stdin.readline().split())
baskets = [0] * basketNum 
for i in range(cnt):
    startNum, lastNum, ballNum = map(int,sys.stdin.readline().split())
    for j in range(startNum-1,lastNum):
        baskets[j] = ballNum
print(*baskets)