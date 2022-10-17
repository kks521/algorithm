
def m4(num):
    return num - 4
def solution(survey,choices):
    result = ''
    choices = list(map(m4,choices))
    score = {'RT': 0 , 'CF': 0, 'JM':0, 'AN':0,'TR':0,'FC':0,'MJ':0,'NA':0}
    for q,s in  zip(survey, choices):
        score[q] += s
    rtscore = - score['RT'] + score['TR']    
    cfscore = - score['CF'] + score['FC']    
    jmscore = - score['JM'] + score['MJ']     
    anscore = - score['AN'] + score['NA']    
    if rtscore >= 0:
        result += 'R'
    else:
        result += 'T'
    if cfscore >= 0:
        result += 'C'
    else:
        result += 'F'
    if jmscore >= 0:
        result += 'J'
    else:
        result += 'M'
    if anscore >= 0:
        result += 'A' 
    else:
        result += 'N'
    return result                
