import sys
checked = [False] * 30 
for i in range(28):
    checked[(int(sys.stdin.readline()))-1] = True
print(checked.index(False)+1)
checked[checked.index(False)] = True
print(checked.index(False)+1)



