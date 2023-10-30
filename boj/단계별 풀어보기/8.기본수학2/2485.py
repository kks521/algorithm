import sys 

cnt = int(sys.stdin.readline())
distances = []
former = int(sys.stdin.readline())

def euclid(a,b):
    r = a % b 
    if r == 0:
        return b
    return euclid(b,r)


for _ in range(cnt-1):
    temp = int(sys.stdin.readline())
    distances.append(temp - former)
    former = temp 

mindistance = distances[0]

for i in range(1,len(distances)):
    mindistance = euclid(mindistance,distances[i])


ans = [x//mindistance -1 for x in distances]
print(sum(ans))