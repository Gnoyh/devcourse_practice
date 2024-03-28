# 큰 수 만들기

def solution(number, k):
    collected = []
    
    for i, v in enumerate(number):
        while len(collected) > 0 and collected[-1] < v and k > 0:
            collected.pop()
            k -= 1
            
        if k == 0:
            collected += list(number[i: ])
            
            break
            
        collected.append(v)
        
    collected = collected[: -k] if k > 0 else collected
    answer = ''.join(collected)
    
    return answer