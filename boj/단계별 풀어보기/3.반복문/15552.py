import sys
test_num = int(sys.stdin.readline())
for i in range(test_num):
    num1, num2 = map(int,sys.stdin.readline().split())
    print(num1 + num2)