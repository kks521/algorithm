import sys 
numlist = []
for i in range(10):
    numlist.append(int(sys.stdin.readline()) % 42)
numlist = set(numlist)
print(len(numlist))
