import sys 

lastNum = int(sys.stdin.readline())
order = list(map(int,sys.stdin.readline().split()))
now = 1 
temp= [lastNum + 1]
ans = 'Nice'
for i in order: 
    if i == now: 
        now += 1
        continue
    while(temp[-1] == now):
        now += 1
        temp.pop()
    if temp[-1] < i:
        ans = 'Sad'
        break
    else:
        temp.append(i)

print(ans)  


