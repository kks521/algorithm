import sys 
numLen = int(sys.stdin.readline())
nums1 = sorted(list(map(int,sys.stdin.readline().split())))
_ = int(sys.stdin.readline())
nums2 = list(map(int,sys.stdin.readline().split()))

def search(num,nums,start,end):
    
    if start > end:
         print(0)
         return
    
    mid = (start + end) // 2

    if nums[mid] == num:
        print(1) 
        return
    elif nums[mid] > num:
        return search(num,nums,start,mid-1)
    else:
        return search(num,nums,mid+1,end)

for i in nums2:
        search(i,nums1,0,numLen-1)     