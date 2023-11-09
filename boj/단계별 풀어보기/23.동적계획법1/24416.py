import sys 

num = int(sys.stdin.readline())

cnt2 = 0 

def solve1(n):
    global cnt1
    if n == 1 or n == 2:  
        cnt1 += 1 
        return 1 
    else: 
        return solve1(n-1) + solve1(n-2)

def solve2(n):
    global cnt2  
    arr = [0,1,1]
    for i in range(3,n+1):
        cnt2 += 1 
        arr.append(arr[i-1] + arr[i-2])
    return arr[-1]



cnt1 = solve2(num)
print(cnt1, cnt2)