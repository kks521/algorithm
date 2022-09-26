import sys 
input()
num = sys.stdin.readline().strip()
result = 0 
for i in num:
    result += int(i)
print(result)