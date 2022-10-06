import sys
case = int(sys.stdin.readline())
list = []
for i in range(case):
    n = int(sys.stdin.readline())
    list.append(n)
for j in sorted(list):
    print(j)