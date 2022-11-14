import sys
m, n = map(int,sys.stdin.readline().split())
bwlist = ['B','W' for i in range(4)]
wblist = reversed(bwlist)
space = []
for i in range(m):
    space.append(list(sys.stdin.readline().strip()))
