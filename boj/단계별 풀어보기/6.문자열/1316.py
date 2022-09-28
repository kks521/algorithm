import sys

case = int(sys.stdin.readline())
check = 0

for i in range(case):
    breakcheck = True
    word = sys.stdin.readline().strip()
    for j in word: 
        if word.count(j) == 1:
            continue
        else:
            j = word.count(j) * j
            if j not in word:
                breakcheck = False
                break
    if breakcheck == False:
        continue
    check += 1         
print(check)