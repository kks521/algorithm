import sys
carddict = {}
n = int(sys.stdin.readline())
cards = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())
nums = map(int,sys.stdin.readline().split())
for i in cards:
    if i in carddict:
        carddict[i] += 1
    else:
        carddict[i] = 1

for j in nums:
    if j not in carddict:
        print(0, end=' ')
    else:
        print(carddict[j],end=' ')