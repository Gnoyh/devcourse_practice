# 예산 소팅

def solution(d, budget):
    result = 0
    
    d.sort()
    
    while (budget >= 0) and result < len(d):
        budget -= d[result]
        
        result += 1
        
    return result - 1 if budget < 0 else result