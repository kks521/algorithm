import sys 

while(1):
    nums = list(map(int,sys.stdin.readline().split()))
    setnums = list(set(nums))
    if setnums[-1] == 0:
        break
    setnums.sort()
    if nums[0] + nums[1] > nums[2]:
        if len(set(setnums)) == 1:
            print('Equilateral')

        elif len(set(setnums)) == 2:
            print('Isosceles')

        else:
            print('Scalene') 
    else: 
        print('Invalid')