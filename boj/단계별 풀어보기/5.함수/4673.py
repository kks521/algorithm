def solve():
    num_list = []
    for i in range(1,10001):
        for j in str(i):
            i += int(j)
        num_list.append(i)    
    for t in range(1,10001):
        if not t in num_list:
            print(t)
solve()