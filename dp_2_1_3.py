# 리스트에서 원소 찾아내기

def solution(L, x):
    result = []
    
    if x in L:
        for i in range(len(L)):
            if L[i] == x:
                result.append(i)
    else:
        result.append(-1)
                
    return result