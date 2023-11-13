import sys 

k, n = map(int,sys.stdin.readline().split())
length = []
for _ in range(k):
    length.append(int(sys.stdin.readline()))

start = 1
end = max(length)
 
while(start <= end):
    mid = (start + end) //2
    line = 0 
    for i in length:
        line += i // mid 

    if line >= n:
        start = mid + 1 
    else: 
        end = mid - 1
print(end)