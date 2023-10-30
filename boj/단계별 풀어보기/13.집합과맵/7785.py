import sys 
cnt = int(sys.stdin.readline())
record = dict()
ans = []

for i in range(cnt):
    name, status  = sys.stdin.readline().strip().split()
    record[name] = status

for n,s in record.items():
    if s == 'enter':
        ans.append(n)
ans.sort(reverse=True)
print(*ans, sep='\n')