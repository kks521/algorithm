import sys 
n = int(sys.stdin.readline())
ans = []
for i in range(n):
    money = int(sys.stdin.readline())
    if money == 0:
        ans.pop()
    else:
        ans.append(money)
print(sum(ans))