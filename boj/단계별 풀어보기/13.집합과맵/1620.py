import sys
n,m = map(int,sys.stdin.readline().split())
pocketmon = list()
num_poc = {}
for i in range(n):
    pocketmon.append(sys.stdin.readline().rstrip())
for num,name in enumerate(pocketmon):
    num_poc[num+1] = name                                                                                  

poc_num = dict(zip(num_poc.values(),num_poc.keys()))

ans = []
for k in range(m):
    check = input()
    if check.isdigit():
        ans.append(num_poc[int(check)])
    else: 
        ans.append(str(poc_num[check]))

print('\n'.join(ans))
