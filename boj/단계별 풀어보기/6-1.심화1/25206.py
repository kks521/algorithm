import sys 

gradeScore = {'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0}
totalCredit = 0
totalScore = 0

for i in range(20):
    subject, credit, grade = sys.stdin.readline().split()
    credit = float(credit)
    if grade == 'P':
        continue
    else:
        totalScore += gradeScore[grade] * credit
        totalCredit += credit

answer = round(totalScore / totalCredit,6)
print(answer)



