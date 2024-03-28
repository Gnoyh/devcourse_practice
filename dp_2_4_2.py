# 체육복

def solution(n, lost, reserve):
    result = n
    u = [1] * (n + 2)
    
    for i in reserve:
        u[i] += 1
        
    for i in lost:
        u[i] -= 1
        
    for i in range(1, n + 1):
        if u[i - 1] == 0 and u[i] == 2:
            u[i - 1: i + 1] = [1, 1]
            result += 1
        elif u[i] == 2 and u[i + 1] == 0:
            u[i: i + 2] = [1, 1]
        elif u[i] == 0:
            result -= 1
            
    return result