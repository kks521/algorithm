import sys 
length = int(sys.stdin.readline())
temp = sys.stdin.readline().strip()

def solve(n):
    return ord(n)-96 

arr = list(map(solve,temp))
ans = 0 

for idx, num in enumerate(arr): 
    ans += num * 31**idx

print(ans % 1234567891 )
