import sys
wb = 'WB'*4
bw = 'BW'*4
wbchess = []
bwchess = []
for i in range(4):
    wbchess.extend([wb,bw])
    bwchess.extend([bw,wb])
n, m = map(int,sys.stdin.readline().split())
space = list()
check = 100
for _ in range(n):
    space.append(sys.stdin.readline().strip())

def checkchess(line,p,status):
        cnt = 0
        for j, k in zip(line,status):
            j = j[p:p+8]
            for l,y in zip(j,k):
                if l != y:
                    cnt += 1 
        return cnt

for i in range(n - 7):
    for j in range(m-7):
        change = checkchess(space[i:i+8],j,wbchess)
        if change <= check:
            check = change
        change = checkchess(space[i:i+8],j,bwchess)
        if change <= check:
            check = change
print(check)