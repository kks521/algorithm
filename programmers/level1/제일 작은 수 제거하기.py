def solution(arr):
    answer = [-1]
    if len(arr) > 1: 
        arr.remove(min(arr))
        return arr
    return answer