def solution(food):
    food.pop(0)
    calorie = 1
    answer = ''
    for i in food: 
        answer += str(calorie) * (i //2)
        calorie += 1  
    answer = answer + '0' + answer[::-1]
    return answer
solution([1, 3, 4, 6])