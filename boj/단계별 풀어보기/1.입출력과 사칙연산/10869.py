import sys
num_1, num_2 = map(int,sys.stdin.readline().split())
print(num_1+num_2,num_1-num_2,num_1 * num_2,num_1//num_2,num_1 % num_2, sep='\n')
