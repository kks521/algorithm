import sys 
global cnt 

def recursion(s, l, r):
    global cnt 
    cnt += 1 
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else:
        return recursion(s, l+1, r-1)
def solve(str):
    return recursion(str,0,len(str)-1)
    
n = int(sys.stdin.readline())
for i in range(n):
    cnt = 0
    word = sys.stdin.readline().strip()
    print(solve(word),cnt)