# 피보나치 순열

def solution(x):
    recursive_result = 0
    iterative_result = 0
    
    # 재귀적 방법
    
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
        
    recursive_result = fibonacci(x)
    
    # 반복적 방법
    
    fibonacci_list = [0, 1]
    
    for i in range(x - 1):
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
            
    iterative_result = fibonacci_list[x]
    
    if recursive_result == iterative_result:
        return recursive_result