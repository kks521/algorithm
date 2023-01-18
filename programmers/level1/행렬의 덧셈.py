def solution(arr1, arr2):
    answer = []
    
    for a,b in zip(arr1,arr2):
        arr3 = []
        for c,d in zip(a,b):
            arr3.append(c+d)
        answer.append(arr3)
    return answer
print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))