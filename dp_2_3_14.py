# 가장 큰 수

def solution(numbers):
    result = ""
    
    numbers.sort(key = lambda x: (str(x) * 4)[: 4], reverse = True)
    
    for i in numbers:
        result += str(i)
        
    return result if result[0] != "0" else "0"