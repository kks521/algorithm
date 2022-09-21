import sys
test_num = int(sys.stdin.readline())
for i in range(test_num):
    num1, num2 = map(int,sys.stdin.readline().split())
    print(f"Case #{i+1}: {num1} + {num2} = {num1 + num2}")