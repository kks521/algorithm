import sys 
n = []
for i in range(3):
    n.append(list(map(int,sys.stdin.readline().split())))
aa = []
bb = []
for s1,s2 in n:
    aa.append(s1)
    bb.append(s2)    

for j in set(aa):
    if aa.count(j) == 1:
        print(j,end=' ')
for k in set(bb):
    if bb.count(k) == 1:
        print(k,end=' ')