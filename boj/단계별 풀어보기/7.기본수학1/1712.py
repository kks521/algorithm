import sys 
fix, variable, price = map(int,sys.stdin.readline().split())
profit = price - variable
if profit <= 0:
    print(-1)
else:
    print(fix // profit + 1)