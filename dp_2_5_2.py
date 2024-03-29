# N으로 표현

def solution(N, number):
    s = [set() for _ in range(8)]
    
    for i, v in enumerate(s, start = 1):
        v.add(int(str(N) * i))
        
    for i in range(8):
        for j in range(i):
            for k in s[j]:
                for l in s[i - j - 1]:
                    s[i].add(k + l)
                    s[i].add(k - l)
                    s[i].add(k * l)
                    
                    if l != 0:
                        s[i].add(k // l)
                        
        if number in s[i]:
            answer = i + 1
            
            break
            
    else:
        answer = -1
    
    return answer