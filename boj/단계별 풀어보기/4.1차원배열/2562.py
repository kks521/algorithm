import sys 
numlist= []
for i in range(9):
    numlist.append(int(sys.stdin.readline()))
print(max(numlist))
print(numlist.index(max(numlist))+1)
