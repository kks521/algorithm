import sys 
def check_vps(vps):
    while vps.count('()') >= 1:
        vps = vps.replace('()','')
    if len(vps) > 0:
        print('NO')
    else:
        print('YES')    
n = int(sys.stdin.readline())
for i in range(n):
    check_vps(sys.stdin.readline().strip())