# 정렬된 리스트에 원소 삽입

def solution(L, x):
    if L[0] >= x:
        L.insert(0, x)
    elif L[-1] <= x:
        L.append(x)
    else:
        for i in range(len(L) - 1):
            if L[i] < x and L[i + 1] >= x:
                L.insert(i + 1, x)
                
    return L