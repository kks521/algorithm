def solution(arr, divisor):
    ans = []
    for num in arr:
        if num % divisor == 0:
            ans.append(num)
    if ans:
        ans.sort()
        return ans
    return [-1]