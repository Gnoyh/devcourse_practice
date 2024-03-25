# 이진탐색

def solution(L, x):
    result = -1
    
    lower = 0
    upper = len(L) - 1
    
    while lower <= upper:
        middle = (lower + upper) // 2
        
        if L[middle] < x:
            lower = middle + 1
        elif L[middle] > x:
            upper = middle - 1
        else:
            return middle
        
    return result