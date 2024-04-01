# 사탕 담기

def solution(m, weights):
    def check_weights(total, n):
        result = 0
        
        if total > m:
            return 0
        elif total == m:
            return 1
        
        for i in range(n, len(weights)):
            result += check_weights(total + weights[i], i + 1)
            
        return result
    
    return check_weights(0, 0)