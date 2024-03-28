# 기능개발

def solution(progresses, speeds):
    days = []
    
    for i in range(len(progresses)):
        days.append((100 - progresses[i]) // speeds[i] if (100 - progresses[i]) % speeds[i] == 0 else (100 - progresses[i]) // speeds[i] + 1)
        
    answer = []
    max_a = days[0]
    count = 0
    
    for i in days:
        if max_a >= i:
            count += 1
        else:
            answer.append(count)
            max_a = i
            count = 1
            
    answer.append(count)
            
    return answer