def solution(sizes):
    maxnum = max(map(max,sizes))
    searchList = [min(i) for i in sizes]
    answer = maxnum * max(searchList)
    return answer
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))