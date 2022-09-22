import sys
cnt = int(sys.stdin.readline())
numlist = list(map(int,sys.stdin.readline().split()))
print(min(numlist),max(numlist))
