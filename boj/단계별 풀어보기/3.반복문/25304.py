import sys 

total_price = int(sys.stdin.readline())
count_num = int(sys.stdin.readline())
check_price = 0 
for i in range(count_num): 
    price, amount = map(int,sys.stdin.readline().split())
    check_price += price * amount
if check_price == total_price:
    print("Yes")
else:
    print("No")