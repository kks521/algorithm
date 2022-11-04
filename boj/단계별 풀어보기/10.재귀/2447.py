import sys
import math as m  
size, saving_time = map(int,sys.stdin.readline().split())
array = list(map(int,sys.stdin.readline().split()))

global count_num 
count_num = 0

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = m.ceil(len(array)/2)
    arr1 = merge_sort(array[:mid])
    arr2 = merge_sort(array[mid:])
    return merge(arr1,arr2)

def merge(arr1,arr2):
    global count_num    
    result = []
    index1 = 0 
    index2 = 0
    while index1 < len(arr1) and index2 < len(arr2):
        if arr1[index1] < arr2[index2]:
            result.append(arr1[index1])
            count_num += 1        
            if count_num == saving_time:
                print(result[-1])
                quit()   
            index1 += 1
        else:
            result.append(arr2[index2])
            count_num += 1        
            if count_num == saving_time:
                print(result[-1])
                quit()
            index2 += 1            

    if index1 == len(arr1):
        while len(arr2) > index2:
            result.append(arr2[index2])
            count_num += 1
            if count_num == saving_time:
                print(result[-1])
                quit() 
            index2 += 1
    if index2 == len(arr2):
        while len(arr1) > index1:
            result.append(arr1[index1])
            count_num += 1
            if count_num == saving_time:
                print(result[-1])
                quit() 
            index1 += 1
    if len(result)== size and saving_time >= count_num:
        print(-1)
        return 
    return result        
                        
merge_sort(array)
